"""Pruebas de seguridad de las cuentas temporales de Praktiko.

Ejecutar: python manage.py test praktiko.tests_demo --verbosity 2
Django crea una base de datos de pruebas independiente.
"""
from concurrent.futures import ThreadPoolExecutor
from threading import Barrier
import hashlib
import hmac

from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import close_old_connections, connections
from django.test import Client, TestCase, TransactionTestCase, override_settings
from django.urls import reverse

from praktiko.models import ControlAltaDemo, SesionDemo


@override_settings(ALLOWED_HOSTS=["testserver"])
class DemoSeguridadTests(TestCase):
    def setUp(self):
        self.pagina = reverse("praktiko:pagina_demo")
        self.inicio = reverse("praktiko:iniciar_demo")

    @override_settings(PRAKTIKO_DEMO_ENABLED=False)
    def test_demo_desactivada_devuelve_404(self):
        self.assertEqual(Client().get(self.pagina).status_code, 404)
        self.assertEqual(Client().post(self.inicio).status_code, 404)
        self.assertEqual(SesionDemo.objects.count(), 0)

    @override_settings(PRAKTIKO_DEMO_ENABLED=True, DEBUG=False)
    def test_pagina_disponible_sin_debug(self):
        self.assertEqual(Client().get(self.pagina).status_code, 200)

    @override_settings(PRAKTIKO_DEMO_ENABLED=True, DEBUG=True, PRAKTIKO_DEMO_MAX_ALTAS_2H=2)
    def test_dos_altas_y_tercera_bloqueada(self):
        # Cada cliente tiene una sesión independiente, pero comparten origen.
        respuestas = [Client(REMOTE_ADDR="198.51.100.10").post(self.inicio) for _ in range(3)]
        self.assertEqual([r.status_code for r in respuestas], [302, 302, 429])
        self.assertEqual(SesionDemo.objects.count(), 2)
        self.assertEqual(ControlAltaDemo.objects.count(), 1)
        self.assertEqual(ControlAltaDemo.objects.get().altas, 2)
        self.assertEqual(get_user_model().objects.filter(username__startswith="pdemo_").count(), 2)

    @override_settings(PRAKTIKO_DEMO_ENABLED=True, DEBUG=True, PRAKTIKO_DEMO_MAX_ALTAS_2H=2)
    def test_origenes_diferentes_tienen_contadores_independientes(self):
        respuestas = [
            Client(REMOTE_ADDR=ip).post(self.inicio).status_code
            for ip in ("198.51.100.10", "198.51.100.10", "198.51.100.10", "198.51.100.11")
        ]
        self.assertEqual(respuestas, [302, 302, 429, 302])
        self.assertEqual(SesionDemo.objects.count(), 3)
        self.assertEqual(ControlAltaDemo.objects.count(), 2)
        self.assertEqual(sorted(ControlAltaDemo.objects.values_list("altas", flat=True)), [1, 2])


@override_settings(
    ALLOWED_HOSTS=["testserver"],
    PRAKTIKO_DEMO_ENABLED=True,
    DEBUG=True,
    PRAKTIKO_DEMO_MAX_ALTAS_2H=2,
)
class DemoConcurrenciaTests(TransactionTestCase):
    """Solicitudes simultáneas con una única alta restante."""

    def test_dos_solicitudes_compiten_por_ultima_alta(self):
        ip = "198.51.100.25"
        inicio = reverse("praktiko:iniciar_demo")
        origen = hmac.new(
            settings.SECRET_KEY.encode(), ip.encode(), hashlib.sha256
        ).hexdigest()

        # La primera alta es secuencial: el registro ya existe al competir.
        primera = Client(REMOTE_ADDR=ip).post(inicio)
        self.assertEqual(primera.status_code, 302)
        self.assertEqual(ControlAltaDemo.objects.get(origen_hash=origen).altas, 1)

        barrera = Barrier(2, timeout=10)

        def solicitud():
            close_old_connections()
            try:
                cliente = Client(REMOTE_ADDR=ip)
                barrera.wait()
                return cliente.post(inicio).status_code
            finally:
                connections.close_all()

        with ThreadPoolExecutor(max_workers=2) as ejecutor:
            resultados = list(ejecutor.map(lambda _: solicitud(), range(2)))

        self.assertEqual(sorted(resultados), [302, 429])
        self.assertEqual(ControlAltaDemo.objects.get(origen_hash=origen).altas, 2)
        self.assertEqual(SesionDemo.objects.count(), 2)
        self.assertEqual(
            get_user_model().objects.filter(username__startswith="pdemo_").count(), 2
        )


@override_settings(PRAKTIKO_DEMO_IA_LIMITE=5)
class DemoLimiteIATests(TestCase):
    """Reservas de IA sin contactar con proveedores externos."""

    def setUp(self):
        from django.utils import timezone
        from datetime import timedelta
        from praktiko.servicios.limite_ia_demo import reservar_solicitud_ia

        self.reservar = reservar_solicitud_ia
        self.usuario = get_user_model().objects.create_user(username="prueba_demo_ia")
        self.sesion = SesionDemo.objects.create(
            usuario=self.usuario, caduca_en=timezone.now() + timedelta(hours=1)
        )

    def test_cinco_reservas_permitidas_y_sexta_denegada(self):
        resultados = [self.reservar(self.usuario) for _ in range(6)]
        self.assertEqual(resultados, [(True, True)] * 5 + [(False, True)])
        self.sesion.refresh_from_db()
        self.assertEqual(self.sesion.solicitudes_ia, 5)

    def test_usuario_normal_sin_limite_demo(self):
        normal = get_user_model().objects.create_user(username="prueba_normal_ia")
        self.assertEqual([self.reservar(normal) for _ in range(7)], [(True, False)] * 7)
        self.sesion.refresh_from_db()
        self.assertEqual(self.sesion.solicitudes_ia, 0)

    def test_sesion_caducada_no_puede_reservar(self):
        from django.utils import timezone
        from datetime import timedelta

        self.sesion.caduca_en = timezone.now() - timedelta(seconds=1)
        self.sesion.save(update_fields=["caduca_en"])
        self.assertEqual(self.reservar(self.usuario), (False, True))
        self.sesion.refresh_from_db()
        self.assertEqual(self.sesion.solicitudes_ia, 0)

    @override_settings(PRAKTIKO_DEMO_IA_LIMITE=0)
    def test_limite_cero_bloquea_todas_las_reservas(self):
        self.assertEqual(self.reservar(self.usuario), (False, True))
        self.sesion.refresh_from_db()
        self.assertEqual(self.sesion.solicitudes_ia, 0)

@override_settings(ALLOWED_HOSTS=["testserver"])
class DemoMiddlewareTests(TestCase):
    """La caducidad solo desconecta cuentas explícitamente marcadas como demo."""

    def test_demo_caducada_se_desconecta_y_redirige(self):
        from datetime import timedelta
        from django.utils import timezone

        usuario = get_user_model().objects.create_user(username="demo_caducada")
        SesionDemo.objects.create(
            usuario=usuario, caduca_en=timezone.now() - timedelta(minutes=1)
        )
        cliente = Client()
        cliente.force_login(usuario)
        respuesta = cliente.get(reverse("praktiko:pagina_demo"))
        self.assertEqual(respuesta.status_code, 302)
        self.assertEqual(respuesta.url, "/praktiko/login/")
        self.assertNotIn("_auth_user_id", cliente.session)

    def test_usuario_normal_conserva_sesion(self):
        usuario = get_user_model().objects.create_user(username="usuario_normal")
        cliente = Client()
        cliente.force_login(usuario)
        # La ruta puede responder 404 si la demo está desactivada;
        # lo que importa es que el middleware no cierre la sesión.
        cliente.get(reverse("praktiko:pagina_demo"))
        self.assertEqual(cliente.session.get("_auth_user_id"), str(usuario.pk))


class DemoLimpiezaTests(TestCase):
    """La limpieza solo elimina cuentas demo caducadas sin privilegios."""

    def test_simulacion_no_borra_y_confirmacion_borra_solo_caducadas(self):
        from datetime import timedelta
        from io import StringIO
        from django.core.management import call_command
        from django.utils import timezone

        User = get_user_model()
        normal = User.objects.create_user(username="normal_limpieza")
        caducado = User.objects.create_user(username="demo_caducado")
        activo = User.objects.create_user(username="demo_activo")
        protegido = User.objects.create_user(username="demo_staff", is_staff=True)
        SesionDemo.objects.create(
            usuario=caducado, caduca_en=timezone.now() - timedelta(hours=1)
        )
        SesionDemo.objects.create(
            usuario=activo, caduca_en=timezone.now() + timedelta(hours=1)
        )
        SesionDemo.objects.create(
            usuario=protegido, caduca_en=timezone.now() - timedelta(hours=1)
        )

        salida = StringIO()
        call_command("limpiar_demos_praktiko", stdout=salida)
        self.assertIn("Cuentas demo caducadas: 2", salida.getvalue())
        self.assertTrue(User.objects.filter(pk=caducado.pk).exists())

        salida = StringIO()
        call_command("limpiar_demos_praktiko", "--confirmar", stdout=salida)
        self.assertIn("Cuentas eliminadas: 1", salida.getvalue())
        self.assertFalse(User.objects.filter(pk=caducado.pk).exists())
        self.assertTrue(User.objects.filter(pk=activo.pk).exists())
        self.assertTrue(User.objects.filter(pk=normal.pk).exists())
        self.assertTrue(User.objects.filter(pk=protegido.pk).exists())