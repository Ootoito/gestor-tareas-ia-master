"""Acceso temporal, DESACTIVADO salvo configuración explícita."""
from datetime import timedelta
import secrets
import hashlib
import hmac
import ipaddress

from django.conf import settings
from django.contrib.auth import get_user_model, login
from django.db import transaction
from django.http import Http404, HttpResponseNotAllowed
from django.shortcuts import redirect, render
from django.utils import timezone

from praktiko.models import Diccionario, Tema, EntradaDiccionario, SesionDemo, ControlAltaDemo



def _consumir_alta_demo(request):
    """Máximo dos altas por IP en una ventana de dos horas.

    En produccion, X-Real-IP solo es fiable si Gunicorn esta aislado y
    Nginx sobrescribe la cabecera con la IP de conexion del cliente.
    No utilizar X-Forwarded-For suministrado por el cliente.
    """
    ip = request.META.get("HTTP_X_REAL_IP", "")
    if not ip and settings.DEBUG:
        # Permite pruebas con runserver, sin proxy inverso.
        ip = request.META.get("REMOTE_ADDR", "")
    try:
        ip = str(ipaddress.ip_address(ip.strip()))
    except (ValueError, AttributeError):
        return False  # Sin IP valida: denegar alta.
    origen = hmac.new(settings.SECRET_KEY.encode(), ip.encode(), hashlib.sha256).hexdigest()
    ahora = timezone.now()
    limite = int(getattr(settings, "PRAKTIKO_DEMO_MAX_ALTAS_2H", 2))
    registro, _ = ControlAltaDemo.objects.select_for_update().get_or_create(
        origen_hash=origen,
        defaults={"ventana_inicio": ahora, "altas": 0},
    )
    if registro.ventana_inicio <= ahora - timedelta(hours=2):
        registro.ventana_inicio = ahora
        registro.altas = 0
    if registro.altas >= max(1, limite):
        return False
    registro.altas += 1
    registro.save(update_fields=["altas", "ventana_inicio"])
    return True


def pagina_demo(request):
    """Pantalla de inicio de una demostracion temporal."""
    if not getattr(settings, "PRAKTIKO_DEMO_ENABLED", False):
        raise Http404("Demostración no disponible")
    return render(request, "praktiko/demo/inicio.html")


def iniciar_demo(request):
    if not getattr(settings, "PRAKTIKO_DEMO_ENABLED", False):
        raise Http404("Demostración no habilitada")
    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])
    if request.user.is_authenticated:
        return redirect("praktiko:home")

    User = get_user_model()
    with transaction.atomic():
        if not _consumir_alta_demo(request):
            return render(request, "praktiko/demo/limite_altas.html", status=429)

        username = "pdemo_" + secrets.token_hex(12)
        user = User(username=username, is_active=True, is_staff=False, is_superuser=False)
        user.set_unusable_password()
        user.save()
        SesionDemo.objects.create(usuario=user, caduca_en=timezone.now() + timedelta(hours=2))
        dic = Diccionario.objects.create(usuario=user, nombre="Inglés de viaje", idioma_origen="Español", idioma_destino="Inglés", descripcion="Vocabulario de demostración")
        tema = Tema.objects.create(usuario=user, diccionario=dic, nombre="Saludos")
        for origen, destino in (("Hola", "Hello"), ("Gracias", "Thank you"), ("Buenos días", "Good morning"), ("Adiós", "Goodbye")):
            EntradaDiccionario.objects.create(usuario=user, diccionario=dic, tema=tema, texto_origen=origen, texto_destino=destino)
    login(request, user, backend="django.contrib.auth.backends.ModelBackend")
    request.session.set_expiry(2 * 60 * 60)
    return redirect("praktiko:home")
