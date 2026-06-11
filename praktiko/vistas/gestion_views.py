import secrets
import string
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render


def es_admin_praktiko(user):
    return (
        user.is_superuser
        or user.groups.filter(name="PraktikoAdmin").exists()
    )


@login_required
def listado_usuarios(request):
    if not es_admin_praktiko(request.user):
        return render(
            request,
            "praktiko/gestion/sin_permiso.html",
            status=403,
        )

    usuarios = (
        User.objects
        .filter(groups__name="Praktiko")
        .annotate(
            total_diccionarios=Count("praktiko_diccionarios", distinct=True),
            total_entradas=Count("praktiko_entradas", distinct=True),
            total_sesiones=Count("praktiko_sesiones", distinct=True),
        )
        .order_by("username")
    )

    return render(
        request,
        "praktiko/gestion/usuarios.html",
        {
            "usuarios": usuarios,
        },
    )

@login_required
def cambiar_estado_usuario(request, usuario_id):
    if not es_admin_praktiko(request.user):
        return render(
            request,
            "praktiko/gestion/sin_permiso.html",
            status=403,
        )

    usuario = get_object_or_404(
        User,
        id=usuario_id,
        groups__name="Praktiko",
    )

    if usuario == request.user:
        messages.error(request, "No puedes desactivarte a ti mismo.")
        return redirect("praktiko:gestion_usuarios")

    usuario.is_active = not usuario.is_active
    usuario.save(update_fields=["is_active"])

    if usuario.is_active:
        messages.success(request, f"Usuario {usuario.username} activado correctamente.")
    else:
        messages.success(request, f"Usuario {usuario.username} desactivado correctamente.")

    return redirect("praktiko:gestion_usuarios")

def generar_password_temporal(longitud=10):
    caracteres = string.ascii_letters + string.digits
    return "".join(secrets.choice(caracteres) for _ in range(longitud))


@login_required
def resetear_password_usuario(request, usuario_id):
    if not es_admin_praktiko(request.user):
        return render(
            request,
            "praktiko/gestion/sin_permiso.html",
            status=403,
        )

    usuario = get_object_or_404(
        User,
        id=usuario_id,
        groups__name="Praktiko",
    )

    nueva_password = generar_password_temporal()
    usuario.set_password(nueva_password)
    usuario.save(update_fields=["password"])

    messages.success(
        request,
        f"Contraseña temporal para {usuario.username}: {nueva_password}",
    )

    return redirect("praktiko:gestion_usuarios")