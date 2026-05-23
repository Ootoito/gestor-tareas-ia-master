# ************************************************************************************
# ********************* SISTEMA DE ALERTAS *******************************************
# ************************************************************************************
from datetime import datetime, timedelta

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import connection
from django.shortcuts import redirect
from django.views.decorators.http import require_POST

from gestor_tareas.vistas.common import validar_acceso_gestor

def read_tipos_alerta():
    sql = """
        SELECT id_tipo_alerta, nombre, minutos_antes
        FROM gestor_tareas_tbtipos_alerta
        WHERE activo = 1
        ORDER BY minutos_antes
    """
    with connection.cursor() as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()

    return [
        {
            "id_tipo_alerta": r[0],
            "nombre": r[1],
            "minutos_antes": r[2],
        }
        for r in rows
    ]

def read_alertas_tarea(id_tarea):
    sql = """
        SELECT a.id_tipo_alerta
        FROM gestor_tareas_tbalertas a
        WHERE a.id_tarea = %s
          AND a.activa = 1
    """
    with connection.cursor() as cursor:
        cursor.execute(sql, [id_tarea])
        rows = cursor.fetchall()

    return [r[0] for r in rows]

def guardar_alertas_tarea(id_tarea, fecha_objetivo_str, tipos_alerta_ids):
    if not fecha_objetivo_str:
        with connection.cursor() as cursor:
            cursor.execute("""
                UPDATE gestor_tareas_tbalertas
                SET activa = 0
                WHERE id_tarea = %s
            """, [id_tarea])
        return

    fecha_objetivo = datetime.strptime(fecha_objetivo_str, "%Y-%m-%dT%H:%M")

    with connection.cursor() as cursor:
        if tipos_alerta_ids:
            placeholders = ",".join(["%s"] * len(tipos_alerta_ids))
            cursor.execute(f"""
                UPDATE gestor_tareas_tbalertas
                SET activa = 0
                WHERE id_tarea = %s
                  AND id_tipo_alerta NOT IN ({placeholders})
            """, [id_tarea] + tipos_alerta_ids)
        else:
            cursor.execute("""
                UPDATE gestor_tareas_tbalertas
                SET activa = 0
                WHERE id_tarea = %s
            """, [id_tarea])

        for id_tipo_alerta in tipos_alerta_ids:
            cursor.execute("""
                SELECT minutos_antes
                FROM gestor_tareas_tbtipos_alerta
                WHERE id_tipo_alerta = %s
            """, [id_tipo_alerta])
            row = cursor.fetchone()
            if not row:
                continue

            minutos_antes = row[0]
            fecha_disparo = fecha_objetivo - timedelta(minutes=minutos_antes)

            cursor.execute("""
                INSERT INTO gestor_tareas_tbalertas
                (id_tarea, id_tipo_alerta, fecha_disparo, activa, lanzada)
                VALUES (%s, %s, %s, 1, 0)
                ON DUPLICATE KEY UPDATE
                    fecha_disparo = VALUES(fecha_disparo),
                    activa = 1,
                    lanzada = 0,
                    fecha_lanzada = NULL
            """, [id_tarea, id_tipo_alerta, fecha_disparo])

def read_alertas_pendientes_para_grupo(id_grupo):
    sql = """
        SELECT
            a.id_alerta,
            t.id,
            t.titulo,
            DATE_FORMAT(t.fecha_objetivo, '%%d/%%m/%%Y %%H:%%i') AS fecha_objetivo,
            ta.nombre AS tipo_alerta,
            a.fecha_disparo
        FROM gestor_tareas_tbalertas a
        INNER JOIN gestor_tareas_tbtareas t
            ON t.id = a.id_tarea
        INNER JOIN gestor_tareas_tbtipos_alerta ta
            ON ta.id_tipo_alerta = a.id_tipo_alerta
        WHERE t.id_grupo = %s
          AND t.activa = 1
          AND a.activa = 1
          AND a.lanzada = 0
          AND a.fecha_disparo <= NOW()
        ORDER BY a.fecha_disparo
    """

    with connection.cursor() as cursor:
        cursor.execute(sql, [id_grupo])
        rows = cursor.fetchall()

    return [
        {
            "id_alerta": r[0],
            "id_tarea": r[1],
            "titulo": r[2],
            "fecha_objetivo": r[3],
            "tipo_alerta": r[4],
            "fecha_disparo": r[5],
        }
        for r in rows
    ]

@login_required
@require_POST
def descartar_alerta(request, id_alerta):
    acceso = validar_acceso_gestor(request)
    if not acceso:
        messages.error(request, "No tienes permiso para acceder al Gestor de tareas.")
        return redirect("login_gestor_tareas")

    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT t.id
            FROM gestor_tareas_tbalertas a
            INNER JOIN gestor_tareas_tbtareas t
                ON t.id = a.id_tarea
            WHERE a.id_alerta = %s
              AND t.id_grupo = %s
            LIMIT 1
        """, [id_alerta, acceso["id_grupo"]])
        row = cursor.fetchone()

        if not row:
            messages.error(request, "No se pudo descartar la alerta.")
            return redirect("gestor_tareas_home")

        cursor.execute("""
            UPDATE gestor_tareas_tbalertas
            SET lanzada = 1,
                fecha_lanzada = NOW()
            WHERE id_alerta = %s
        """, [id_alerta])

    messages.success(request, "Alerta descartada.")
    return redirect("gestor_tareas_home")


