# ************************************************************************************************
# *********************** PARA FICHERO COMMONS.PY (FUNCIONES COMPARTIDAS) ************************
# ************************************************************************************************

from django.contrib.auth.models import User
from django.db import connection
from django.shortcuts import redirect
from django.contrib import messages

from gestor_tareas.models import (
    UsuarioGestor,
    UsuarioGrupo,
)

def validar_acceso_gestor(request):
    if not request.user.is_authenticated:
        return None

    try:
        perfil = UsuarioGestor.objects.select_related("user").get(
            user=request.user,
            activo=True,
        )
    except UsuarioGestor.DoesNotExist:
        return None

    grupos_usuario = read_grupos_usuario(request.user.username)
    if not grupos_usuario:
        return None

    grupo_sesion = request.session.get("gestor_tareas_id_grupo")
    try:
        grupo_sesion = int(grupo_sesion) if grupo_sesion is not None else None
    except (TypeError, ValueError):
        grupo_sesion = None

    ids_grupos_permitidos = [g["id_grupo"] for g in grupos_usuario]

    if grupo_sesion is None or grupo_sesion not in ids_grupos_permitidos:
        grupo_activo = grupos_usuario[0]
    else:
        grupo_activo = next(
            (g for g in grupos_usuario if g["id_grupo"] == grupo_sesion),
            grupos_usuario[0]
        )

    grupo_anterior = request.session.get("gestor_tareas_id_grupo")
    try:
        grupo_anterior = int(grupo_anterior) if grupo_anterior is not None else None
    except (TypeError, ValueError):
        grupo_anterior = None

    if grupo_anterior is not None and grupo_anterior != grupo_activo["id_grupo"]:
        request.session.pop("gestor_tareas_filtros", None)

    alias = perfil.alias or request.user.username

    request.session["gestor_tareas_alias"] = alias
    request.session["gestor_tareas_id_grupo"] = grupo_activo["id_grupo"]
    request.session["gestor_tareas_grupo"] = grupo_activo["nombre"]

    return {
        "alias": alias,
        "id_grupo": grupo_activo["id_grupo"],
        "grupo": grupo_activo["nombre"],
        "grupos_usuario": grupos_usuario,
    }

def read_grupos_usuario(usuario):
    relaciones = (
        UsuarioGrupo.objects
        .select_related("grupo", "usuario")
        .filter(
            usuario__username__iexact=usuario,
            activo=True,
            grupo__activo=True,
        )
        .order_by("grupo__nombre")
    )

    return [
        {"id_grupo": r.grupo.id, "nombre": r.grupo.nombre}
        for r in relaciones
    ]

def usuario_es_admin_gestor(user):
    if not user.is_authenticated:
        return False

    if user.is_superuser:
        return True

    return UsuarioGestor.objects.filter(
        user=user,
        activo=True,
        es_admin_gestor=True,
    ).exists()