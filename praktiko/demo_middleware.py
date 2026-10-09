"""Caducidad obligatoria de usuarios de demostración de Praktiko.

Se ejecuta después de AuthenticationMiddleware. No elimina datos.
"""
from django.contrib.auth import logout
from django.http import HttpResponseForbidden
from django.shortcuts import redirect
from django.utils import timezone

from praktiko.models import SesionDemo


class CaducidadDemoMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user = request.user
        if user.is_authenticated:
            # No basarse en el prefijo del nombre: solo cuentas registradas.
            sesion = SesionDemo.objects.filter(usuario_id=user.pk).only('caduca_en').first()
            if sesion is not None and sesion.caduca_en <= timezone.now():
                logout(request)
                if request.path_info.startswith('/praktiko/'):
                    if request.method in ('GET', 'HEAD'):
                        return redirect('/praktiko/login/')
                    return HttpResponseForbidden('La demostración ha caducado. Inicia otra desde el acceso de demostración.')
                return HttpResponseForbidden('La demostración ha caducado.')
        return self.get_response(request)
