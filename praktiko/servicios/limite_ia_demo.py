"""Reserva atómica de solicitudes de IA para demostraciones."""
from django.conf import settings
from django.db import transaction
from django.db.models import F
from django.utils import timezone
from praktiko.models import SesionDemo


def reservar_solicitud_ia(usuario):
    """(permitida, es_demo). Cuenta intentos antes de contactar con el proveedor."""
    limite = max(0, int(getattr(settings, "PRAKTIKO_DEMO_IA_LIMITE", 5)))
    with transaction.atomic():
        demo = SesionDemo.objects.filter(usuario_id=usuario.pk).first()
        if demo is None:
            return True, False
        if demo.caduca_en <= timezone.now():
            return False, True
        # UPDATE condicional atómico: dos peticiones simultáneas no superan el límite.
        actualizadas = SesionDemo.objects.filter(
            pk=demo.pk, caduca_en__gt=timezone.now(), solicitudes_ia__lt=limite
        ).update(solicitudes_ia=F("solicitudes_ia") + 1)
        return bool(actualizadas), True
