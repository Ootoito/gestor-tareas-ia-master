import hashlib
import logging

from django.conf import settings
from django.core.cache import cache
from django.core.mail import EmailMessage
from django.http import HttpResponseNotAllowed
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .forms import ContactoForm
from .models import Proyecto

logger = logging.getLogger(__name__)


def _render_inicio(request, formulario=None, estado_contacto=None):
    proyectos_destacados = Proyecto.objects.filter(destacado=True)
    return render(request, 'portfolio/inicio.html', {
        'proyectos_destacados': proyectos_destacados,
        'formulario_contacto': formulario or ContactoForm(),
        'estado_contacto': estado_contacto,
    })


def inicio(request):
    return _render_inicio(request)


@require_POST
def contacto(request):
    formulario = ContactoForm(request.POST)
    if not formulario.is_valid():
        return _render_inicio(request, formulario, 'error_validacion')

    # Honeypot: responder sin enviar nada para no ayudar a los bots.
    if formulario.cleaned_data['web']:
        return _render_inicio(request, estado_contacto='enviado')

    # Usar REMOTE_ADDR: no confiar en cabeceras X-Forwarded-For arbitrarias.
    ip = request.META.get('REMOTE_ADDR', 'desconocida')
    clave = 'portfolio_contacto:' + hashlib.sha256(ip.encode('utf-8')).hexdigest()
    limite = max(1, int(getattr(settings, 'PORTFOLIO_CONTACTO_MAX_POR_HORA', 3)))
    if not cache.add(clave, 1, timeout=3600):
        try:
            cantidad = cache.incr(clave)
        except ValueError:
            cantidad = limite + 1
    else:
        cantidad = 1
    if cantidad > limite:
        return _render_inicio(request, formulario, 'limite')

    datos = formulario.cleaned_data
    destinatario = getattr(settings, 'PORTFOLIO_CONTACTO_DESTINATARIO', 'ootoito.totoy@gmail.com')
    asunto = '[Portfolio] ' + datos['asunto'].replace('\n', ' ').replace('\r', ' ')
    cuerpo = (
        f"Nombre: {datos['nombre']}\n"
        f"Correo: {datos['correo']}\n"
        f"Asunto: {datos['asunto']}\n\n"
        f"Mensaje:\n{datos['mensaje']}\n"
    )
    try:
        correo = EmailMessage(asunto, cuerpo, settings.DEFAULT_FROM_EMAIL, [destinatario], reply_to=[datos['correo']])
        correo.send(fail_silently=False)
    except Exception:
        logger.exception('No se pudo enviar un mensaje desde el formulario del portfolio')
        return _render_inicio(request, formulario, 'error_envio')
    return redirect('/portfolio/?contacto=enviado#contacto')


def detalle_proyecto(request, slug):
    proyecto = get_object_or_404(Proyecto, slug=slug)
    return render(request, 'portfolio/detalle_proyecto.html', {'proyecto': proyecto})
