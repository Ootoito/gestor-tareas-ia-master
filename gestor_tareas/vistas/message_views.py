# **************************************************************************
# ************* MENSAJERÍA INTERNA DEL GESTOR DE TAREAS ********************
# **************************************************************************
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.utils import timezone
from gestor_tareas.models import *

from gestor_tareas.vistas.common import validar_acceso_gestor, read_grupos_usuario, usuario_es_admin_gestor

@login_required
def mensajes_gestor(request):
    acceso = validar_acceso_gestor(request)

    if not acceso:
        messages.error(request, "No tienes permiso para acceder al gestor.")
        return redirect("login_gestor_tareas")

    usuarios = User.objects.filter(is_active=True).order_by("username")
    grupos_usuario = read_grupos_usuario(request.user.username)

    mensajes_recibidos = (
        MensajeGestor.objects
        .select_related("remitente", "destinatario", "grupo")
        .filter(destinatario=request.user)
        .order_by("-fecha_envio")
    )

    mensajes_enviados = (
        MensajeGestor.objects
        .select_related("remitente", "destinatario", "grupo")
        .filter(remitente=request.user)
        .order_by("-fecha_envio")[:20]
    )

    if request.method == "POST":
        accion = request.POST.get("accion", "").strip()

        if accion == "enviar_mensaje":
            asunto = request.POST.get("asunto", "").strip()
            cuerpo = request.POST.get("cuerpo", "").strip()
            id_destinatario = request.POST.get("id_destinatario", "").strip()
            envio_global = request.POST.get("envio_global") == "1"

            if not asunto:
                messages.error(request, "Debes indicar el asunto.")
            elif not cuerpo:
                messages.error(request, "Debes escribir el mensaje.")
            elif envio_global and not usuario_es_admin_gestor(request.user):
                messages.error(request, "Solo los administradores pueden enviar mensajes globales.")
            else:
                if envio_global:
                    destinatarios = User.objects.filter(is_active=True).exclude(id=request.user.id)

                    for usuario in destinatarios:
                        MensajeGestor.objects.create(
                            remitente=request.user,
                            destinatario=usuario,
                            grupo_id=acceso["id_grupo"],
                            asunto=asunto,
                            cuerpo=cuerpo,
                        )

                    messages.success(request, "Mensaje enviado a todos los usuarios.")
                else:
                    if not id_destinatario:
                        messages.error(request, "Debes seleccionar destinatario.")
                    else:
                        destinatario = User.objects.get(id=id_destinatario)

                        MensajeGestor.objects.create(
                            remitente=request.user,
                            destinatario=destinatario,
                            grupo_id=acceso["id_grupo"],
                            asunto=asunto,
                            cuerpo=cuerpo,
                        )

                        messages.success(request, "Mensaje enviado correctamente.")

            return redirect("mensajes_gestor")

    context = {
        "usuarios": usuarios,
        "mensajes_recibidos": mensajes_recibidos,
        "mensajes_enviados": mensajes_enviados,
        "usuario_es_admin": usuario_es_admin_gestor(request.user),
        "grupos_usuario": grupos_usuario,
        "grupo_activo": acceso["id_grupo"],
        "grupo_activo_nombre": acceso["grupo"],
    }

    return render(request, "gestortareas/mensajes_gestor.html", context)


@login_required
def marcar_mensaje_leido(request, id_mensaje):
    mensaje = MensajeGestor.objects.filter(
        id_mensaje=id_mensaje,
        destinatario=request.user,
    ).first()

    if mensaje:
        mensaje.leido = True
        mensaje.save()

    return redirect("mensajes_gestor")

@login_required
def detalle_mensaje(request, id_mensaje):

    acceso = validar_acceso_gestor(request)

    if not acceso:
        messages.error(request, "No tienes acceso.")
        return redirect("login_gestor_tareas")

    mensaje = get_object_or_404(
        MensajeGestor.objects.select_related(
            "remitente",
            "destinatario",
            "grupo",
        ),
        id_mensaje=id_mensaje,
    )

    if mensaje.destinatario != request.user and mensaje.remitente != request.user:
        messages.error(request, "No puedes acceder a este mensaje.")
        return redirect("mensajes_gestor")

    if mensaje.destinatario == request.user and not mensaje.leido:
        mensaje.leido = True
        mensaje.save()

    perfil = PerfilUsuario.objects.filter(
        usuario=mensaje.remitente
    ).first()

    context = {
        "mensaje": mensaje,
        "perfil_remitente": perfil,
    }

    return render(
        request,
        "gestortareas/detalle_mensaje.html",
        context
    )