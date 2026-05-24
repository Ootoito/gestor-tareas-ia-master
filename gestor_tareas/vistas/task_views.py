# **********************************************************************************************
# ********************** TAREAS ****************************************************************
# **********************************************************************************************
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import connection
from django.shortcuts import redirect
from django.views.decorators.http import require_POST

from gestor_tareas.vistas.common import validar_acceso_gestor
from gestor_tareas.views import read_tasks, registrar_auditoria

@login_required
@require_POST
def eliminar_tarea(request, tarea_id):
    acceso = validar_acceso_gestor(request)
    if not acceso:
        messages.error(request, "No tienes permiso o grupo asignado para Gestor de tareas.")
        return redirect("/")

    sql = """
        UPDATE gestor_tareas_tbtareas
        SET activa = 0
        WHERE id = %s
          AND id_grupo = %s
    """

    with connection.cursor() as cursor:
        cursor.execute(sql, [tarea_id, acceso["id_grupo"]])

    registrar_auditoria(
        id_tarea=tarea_id,
        accion="ELIMINAR",
        campo="activa",
        valor_anterior="1",
        valor_nuevo="0",
        usuario=request.user.username,
        observaciones=f"Eliminación lógica por {acceso['alias']}"
    )

    messages.success(request, "Tarea eliminada.")
    return redirect("gestor_tareas_home")

@login_required
@require_POST
def anadir_nota(request, tarea_id):
    acceso = validar_acceso_gestor(request)
    if not acceso:
        messages.error(request, "No tienes permiso para acceder al Gestor de tareas.")
        return redirect("login_gestor_tareas")

    texto = request.POST.get("texto_nota", "").strip()
    if not texto:
        messages.error(request, "Debes escribir el texto de la nota.")
        return redirect("detalle_tarea", tarea_id=tarea_id)

    tareas = read_tasks(id_grupo=acceso["id_grupo"])
    existe = any(int(t.get("id", 0)) == int(tarea_id) for t in tareas)

    if not existe:
        messages.error(request, "No puedes añadir notas a esta tarea.")
        return redirect("gestor_tareas_home")

    insertar_nota_tarea(
        id_tarea=tarea_id,
        usuario=request.user.username,
        texto=texto,
    )

    registrar_auditoria(
        id_tarea=tarea_id,
        accion="AÑADIR_NOTA",
        campo="nota",
        valor_anterior="",
        valor_nuevo=texto,
        usuario=request.user.username,
        observaciones=f"Nota añadida por {acceso['alias']}"
    )

    messages.success(request, "Nota añadida correctamente.")
    return redirect("detalle_tarea", tarea_id=tarea_id)

def insertar_nota_tarea(id_tarea, usuario, texto):
    sql = """
        INSERT INTO gestor_tareas_tbnotas
        (id_tarea, fecha, usuario, texto)
        VALUES (%s, NOW(), %s, %s)
    """

    with connection.cursor() as cursor:
        cursor.execute(sql, [id_tarea, usuario, texto])

def cambiar_grupo(request):
    nuevo_grupo = request.POST.get("grupo")
    request.session["gestor_tareas_id_grupo"] = int(nuevo_grupo)
    return redirect("gestor_tareas_home")