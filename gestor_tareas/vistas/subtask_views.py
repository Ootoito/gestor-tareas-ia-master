# *********************************************************************************
# ******************* VISTAS DE SUBTAREAS *****************************************
# *********************************************************************************
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django.views.decorators.http import require_POST

from gestor_tareas.models import Subtarea
from gestor_tareas.vistas.common import validar_acceso_gestor


@login_required
@require_POST
def toggle_subtarea(request, id_subtarea):
    acceso = validar_acceso_gestor(request)
    if not acceso:
        messages.error(request, "No tienes permiso para acceder al Gestor de tareas.")
        return redirect("login_gestor_tareas")

    subtarea = get_object_or_404(
        Subtarea.objects.select_related("tarea"),
        id_subtarea=id_subtarea,
        tarea__grupo_id=acceso["id_grupo"],
    )

    subtarea.completada = not subtarea.completada
    subtarea.save()

    return redirect("detalle_tarea", tarea_id=subtarea.tarea_id)

@login_required
@require_POST
def eliminar_subtarea(request, id_subtarea):
    acceso = validar_acceso_gestor(request)
    if not acceso:
        messages.error(request, "No tienes permiso para acceder al Gestor de tareas.")
        return redirect("login_gestor_tareas")

    subtarea = get_object_or_404(
        Subtarea.objects.select_related("tarea"),
        id_subtarea=id_subtarea,
        tarea__grupo_id=acceso["id_grupo"],
    )

    tarea_id = subtarea.tarea_id
    subtarea.delete()

    messages.success(request, "Subtarea eliminada.")
    return redirect("detalle_tarea", tarea_id=tarea_id)