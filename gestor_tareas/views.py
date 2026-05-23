from __future__ import annotations
import os

# REFACTORIZANDO - PROPUESTO BORRAR - from urllib import request
# REFACTORIZANDO - PROPUESTO BORRAR - from httpx import request

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.db import connection
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST
from datetime import datetime, timedelta


from .models import (
    TecnicoGrupo,
    UsuarioGestor,
    UsuarioGrupo,
    Tarea,
    EstadoTarea,
    AmbitoTarea,
    Tecnico,
    GrupoTrabajo,
    UsuarioRolGestor,
    Subtarea,
    PerfilUsuario,
    MensajeGestor,
)
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.db.models import Count
from django.utils import timezone
from django.contrib.auth.models import User
from django.db import transaction
from .services.ia import (
    generar_resumen_ia_gestor,
    generar_subtareas_ia,
    analizar_prioridad_ia,
)
from pathlib import Path
from django.conf import settings

from gestor_tareas.vistas.common import (
    validar_acceso_gestor,
    read_grupos_usuario,
    usuario_es_admin_gestor,
)

# **********************************************************************************************
# ************* TEMPORAL DURANTE LA REFACTORIZACIÓN - PARA ELIMINAR DESPUÉS ********************
# **********************************************************************************************
from gestor_tareas.vistas.alert_views import (
    read_alertas_pendientes_para_grupo,
    read_tipos_alerta,
    read_alertas_tarea,
    guardar_alertas_tarea,
)

from gestor_tareas.vistas.common import validar_acceso_gestor

from gestor_tareas.services.usuarios import (
    crear_o_actualizar_usuario_gestor,
    sincronizar_usuario_como_tecnico_en_grupo,
)

# =========================================================
# Constantes
# =========================================================

# Pon aquí el ID real de la actuación del gestor
ID_ACTUACION_GESTOR_TAREAS = 908
PRIORIDADES = ["Baja", "Normal", "Alta", "Urgente"]




# =========================================================
# HELPERS / Servicios IA
# =========================================================

# =========================================================
# Catálogos desde BD
# =========================================================

def read_estados(id_grupo=None):
    queryset = EstadoTarea.objects.filter(activo=True)

    if id_grupo is not None:
        queryset = queryset.filter(grupo_id=id_grupo)

    return list(
        queryset
        .order_by("orden", "nombre")
        .values_list("nombre", flat=True)
    )

def read_ambitos():
    sql = """
        SELECT nombre
        FROM gestor_tareas_tbambitos
        WHERE activo = 1
        ORDER BY nombre
    """
    with connection.cursor() as cursor:
        cursor.execute(sql)
        return [row[0] for row in cursor.fetchall()]

def read_tecnicos(id_grupo=None):
    sql = """
        SELECT DISTINCT t.nombre
        FROM gestor_tareas_tbtecnicos t
        INNER JOIN gestor_tareas_tbtecnicos_grupos tg
            ON tg.id_tecnico = t.id_tecnico
        WHERE t.activo = 1
          AND tg.activo = 1
    """
    params = []

    if id_grupo is not None:
        sql += " AND tg.id_grupo = %s"
        params.append(id_grupo)

    sql += " ORDER BY t.nombre"

    with connection.cursor() as cursor:
        cursor.execute(sql, params)
        return [row[0] for row in cursor.fetchall()]


# =========================================================
# Auditoría
# =========================================================

def registrar_auditoria(id_tarea, accion, campo=None, valor_anterior=None, valor_nuevo=None, usuario=None, observaciones=None):
    sql = """
        INSERT INTO gestor_tareas_tbauditoria
        (
            id_tarea,
            usuario,
            accion,
            campo,
            valor_anterior,
            valor_nuevo,
            observaciones
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """

    with connection.cursor() as cursor:
        cursor.execute(sql, [
            id_tarea,
            usuario,
            accion,
            campo,
            valor_anterior,
            valor_nuevo,
            observaciones
        ])


# =========================================================
# Tareas
# =========================================================

def read_tasks(id_grupo=None):

    queryset = (
        Tarea.objects
        .select_related(
            "estado",
            "ambito",
            "tecnico",
            "grupo",
        )
        .filter(activa=True)
        .order_by("-id")
    )

    if id_grupo is not None:
        queryset = queryset.filter(grupo_id=id_grupo)

    tareas = []

    for t in queryset:

        fecha_formateada = ""
        if t.fecha:
            fecha_formateada = t.fecha.strftime("%d/%m/%Y")

        fecha_objetivo = ""
        if t.fecha_objetivo:
            fecha_objetivo = t.fecha_objetivo.strftime("%Y-%m-%dT%H:%M")

        tareas.append({
            "id": t.id,
            "numero_tarea": t.numero_tarea,
            "fecha_creacion": fecha_formateada,
            "fecha": fecha_formateada,
            "estado": t.estado.nombre if t.estado else "",
            "estado_color": t.estado.color if t.estado else "#6c757d",
            "prioridad": t.prioridad or "Normal",
            "ambito": t.ambito.nombre if t.ambito else "",
            "tecnico": t.tecnico.nombre if t.tecnico else "",
            "titulo": t.titulo or "",
            "descripcion": t.descripcion or "",
            "fecha_objetivo": fecha_objetivo,
        })

    return tareas


def insertar_tarea(fecha, estado, prioridad, ambito, tecnico, titulo, descripcion, id_grupo, usuario_creador):
    fecha_obj = datetime.strptime(fecha, "%d/%m/%Y").date()

    grupo = GrupoTrabajo.objects.get(id=id_grupo)

    estado_obj = EstadoTarea.objects.filter(
        nombre=estado,
        activo=True,
    ).first()

    ambito_obj = AmbitoTarea.objects.filter(
        nombre=ambito,
        activo=True,
    ).first()

    tecnico_obj = None
    if tecnico:
        tecnico_obj = Tecnico.objects.filter(
            nombre=tecnico,
            activo=True,
        ).first()

    ultimo_numero = (
        Tarea.objects
        .filter(
            grupo=grupo,
            fecha__year=fecha_obj.year,
        )
        .order_by("-numero_tarea")
        .values_list("numero_tarea", flat=True)
        .first()
    )

    numero_tarea = (ultimo_numero or 0) + 1

    tarea = Tarea.objects.create(
        numero_tarea=numero_tarea,
        fecha=fecha_obj,
        estado=estado_obj,
        prioridad=prioridad or "Normal",
        ambito=ambito_obj,
        tecnico=tecnico_obj,
        grupo=grupo,
        titulo=titulo,
        descripcion=descripcion,
        usuario_creador=usuario_creador,
        activa=True,
    )

    return {
        "id": tarea.id,
        "numero_tarea": tarea.numero_tarea,
    }

# =========================================================
# Vistas
# =========================================================

@login_required
def gestor_tareas_home(request):
    acceso = validar_acceso_gestor(request)
    # DEBUB PARA ELIMINAR INICIO
    #print("DEBUG acceso =", acceso)
    # DEBUB PARA ELIMINAR FIN
    if not acceso:
        messages.error(request, "No tienes permiso o grupo asignado para Gestor de tareas (crtlAcceso).")
        return redirect("login_gestor_tareas")

    id_grupo = acceso["id_grupo"]
    grupos_usuario = read_grupos_usuario(request.user.username)
    ids_grupos_usuario = [g["id_grupo"] for g in grupos_usuario]

    if id_grupo not in ids_grupos_usuario and ids_grupos_usuario:
        id_grupo = ids_grupos_usuario[0]
        request.session["gestor_tareas_id_grupo"] = id_grupo

    # DEBUB PARA ELIMINAR INICIO
    #print("DEBUG id_grupo cargado =", id_grupo)
    # DEBUB PARA ELIMINAR FIN

    tareas = read_tasks(id_grupo=id_grupo)
    # DEBUB PARA ELIMINAR INICIO
    #print("DEBUG num tareas cargadas =", len(tareas))
    #if tareas:
    #print("DEBUG primera tarea =", tareas[0])
    # DEBUB PARA ELIMINAR FIN
    alertas_pendientes = read_alertas_pendientes_para_grupo(id_grupo)
    estados = read_estados(id_grupo=id_grupo)
    ambitos = read_ambitos()
    tecnicos = read_tecnicos(id_grupo=acceso["id_grupo"])

    if request.GET.get("clear") == "1":
        request.session.pop("gestor_tareas_filtros", None)

    filtros_session = request.session.get("gestor_tareas_filtros", {})

    hay_parametros_filtro = any(
        k in request.GET for k in ["estado", "ambito", "tecnico", "q", "ocultar_estados"]
    )

    if hay_parametros_filtro:
        estado_filtro = request.GET.get("estado", "").strip()
        ambito_filtro = request.GET.get("ambito", "").strip()
        tecnico_filtro = request.GET.get("tecnico", "").strip()
        q = request.GET.get("q", "").strip()
        ocultar_estados = request.GET.getlist("ocultar_estados")

        filtros = {
            "estado": estado_filtro,
            "ambito": ambito_filtro,
            "tecnico": tecnico_filtro,
            "q": q,
            "ocultar_estados": ocultar_estados,
        }

        request.session["gestor_tareas_filtros"] = filtros
    else:
        estado_filtro = filtros_session.get("estado", "")
        ambito_filtro = filtros_session.get("ambito", "")
        tecnico_filtro = filtros_session.get("tecnico", "")
        q = filtros_session.get("q", "")
        ocultar_estados = filtros_session.get("ocultar_estados", [])

        filtros = {
            "estado": estado_filtro,
            "ambito": ambito_filtro,
            "tecnico": tecnico_filtro,
            "q": q,
            "ocultar_estados": ocultar_estados,
        }

    tareas_filtradas = tareas[:]

    if estado_filtro:
        tareas_filtradas = [t for t in tareas_filtradas if t.get("estado", "") == estado_filtro]

    if ambito_filtro:
        tareas_filtradas = [t for t in tareas_filtradas if t.get("ambito", "") == ambito_filtro]

    if tecnico_filtro:
        tareas_filtradas = [t for t in tareas_filtradas if t.get("tecnico", "") == tecnico_filtro]

    if q:
        q_lower = q.lower()
        tareas_filtradas = [
            t for t in tareas_filtradas
            if q_lower in str(t.get("titulo", "")).lower()
            or q_lower in str(t.get("descripcion", "")).lower()
        ]

    if ocultar_estados:
        tareas_filtradas = [
            t for t in tareas_filtradas
            if t.get("estado", "") not in ocultar_estados
        ]

    queryset_dashboard = Tarea.objects.filter(
        activa=True,
        grupo_id=id_grupo,
    )

    total_tareas = queryset_dashboard.count()

    contadores_estados = []

    estados_grupo = EstadoTarea.objects.filter(
        grupo_id=id_grupo,
        activo=True
    ).order_by("orden", "nombre")

    for estado in estados_grupo:

        total_estado = queryset_dashboard.filter(
            estado=estado
        ).count()

        contadores_estados.append({
            "nombre": estado.nombre,
            "total": total_estado,
            "color": estado.color,
        })

    tareas_por_tecnico = (
        queryset_dashboard
        .values("tecnico__nombre")
        .annotate(total=Count("id"))
        .order_by("-total")
    )

    alertas_pendientes = read_alertas_pendientes_para_grupo(id_grupo)

# DEBUB PARA ELIMINAR INICIO
    #print("DEBUG filtros =", filtros)
    #print("DEBUG num tareas filtradas =", len(tareas_filtradas))
# DEBUB PARA ELIMINAR FIN

    mensajes_no_leidos = (
        MensajeGestor.objects
        .select_related("remitente")
        .filter(
            destinatario=request.user,
            leido=False,
        )
        .order_by("-fecha_envio")
    )

    total_mensajes_no_leidos = mensajes_no_leidos.count()

    context = {
        "tareas": tareas_filtradas,
        "estados": estados,
        "ambitos": ambitos,
        "tecnicos": tecnicos,
        "filtros": filtros,
        "usuario_alias": acceso["alias"],
        "total_tareas": total_tareas,
        "contadores_estados": contadores_estados,
        "alertas_pendientes": alertas_pendientes,
        "grupos_usuario": grupos_usuario,
        "grupo_activo": acceso["id_grupo"],
        "grupo_activo_nombre": acceso["grupo"],
        "tareas_por_tecnico": tareas_por_tecnico,
        "mensajes_no_leidos": mensajes_no_leidos[:3],
        "total_mensajes_no_leidos": total_mensajes_no_leidos,
    }

    return render(request, "gestortareas/gestor_tareas.html", context)

def read_notas_tarea(id_tarea):
    sql = """
        SELECT
            id_nota,
            DATE_FORMAT(fecha, '%%d/%%m/%%Y %%H:%%i') AS fecha,
            usuario,
            texto
        FROM gestor_tareas_tbnotas
        WHERE id_tarea = %s
          AND activa = 1
        ORDER BY fecha ASC, id_nota ASC
    """

    with connection.cursor() as cursor:
        cursor.execute(sql, [id_tarea])
        rows = cursor.fetchall()

    return [
        {
            "id_nota": r[0],
            "fecha": r[1],
            "usuario": r[2],
            "texto": r[3],
        }
        for r in rows
    ]





@login_required
def nueva_tarea(request):
    acceso = validar_acceso_gestor(request)
    if not acceso:
        messages.error(request, "No tienes permiso o grupo asignado para Gestor de tareas.")
        return redirect("login_gestor_tareas")

    if request.method == "POST":
        fecha = request.POST.get("fecha", "").strip()
        estado = request.POST.get("estado", "").strip() or "Pendiente"
        prioridad = request.POST.get("prioridad", "").strip() or "Normal"
        ambito = request.POST.get("ambito", "").strip() or "Otros"
        tecnico = request.POST.get("tecnico", "").strip()
        titulo = request.POST.get("titulo", "").strip()
        descripcion = request.POST.get("descripcion", "").strip()

        if not fecha:
            messages.error(request, "Debes indicar la fecha.")
        elif not titulo:
            messages.error(request, "Debes indicar el título.")
        else:
            resultado = insertar_tarea(
                fecha=fecha,
                estado=estado,
                prioridad=prioridad,
                ambito=ambito,
                tecnico=tecnico,
                titulo=titulo,
                descripcion=descripcion,
                id_grupo=acceso["id_grupo"],
                usuario_creador=request.user.username,
            )

            id_tarea = resultado["id"]

            registrar_auditoria(
                id_tarea=id_tarea,
                accion="CREAR",
                campo=None,
                valor_anterior=None,
                valor_nuevo=titulo,
                usuario=request.user.username,
                observaciones=f"Alta de tarea por {acceso['alias']}"
            )

            messages.success(request, "Tarea creada correctamente.")
            return redirect("detalle_tarea", tarea_id=id_tarea)

    context = {
        "estados": read_estados(id_grupo=acceso["id_grupo"]),
        "ambitos": read_ambitos(),
        "tecnicos": read_tecnicos(id_grupo=acceso["id_grupo"]),
        "prioridades": PRIORIDADES,
        "hoy": datetime.now().strftime("%d/%m/%Y"),
    }

    return render(request, "gestortareas/nueva_tarea.html", context)



@login_required
@require_POST
def cambiar_estado(request, tarea_id):
    acceso = validar_acceso_gestor(request)
    if not acceso:
        messages.error(request, "No tienes permiso o grupo asignado para Gestor de tareas.")
        return redirect("/")

    nuevo_estado = request.POST.get("nuevo_estado", "").strip()
    if not nuevo_estado:
        messages.error(request, "Debes seleccionar un estado.")
        return redirect("gestor_tareas_home")

    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT e.nombre
            FROM gestor_tareas_tbtareas t
            LEFT JOIN gestor_tareas_tbestados e
                ON t.id_estado = e.id_estado
            WHERE t.id = %s
              AND t.id_grupo = %s
        """, [tarea_id, acceso["id_grupo"]])
        row = cursor.fetchone()
        estado_anterior = row[0] if row else ""

        cursor.execute("""
            SELECT id_estado
            FROM gestor_tareas_tbestados
            WHERE nombre = %s
            LIMIT 1
        """, [nuevo_estado])
        row = cursor.fetchone()
        if not row:
            messages.error(request, "Estado no válido.")
            return redirect("gestor_tareas_home")

        id_estado_nuevo = row[0]

        cursor.execute("""
            UPDATE gestor_tareas_tbtareas
            SET id_estado = %s
            WHERE id = %s
              AND id_grupo = %s
        """, [id_estado_nuevo, tarea_id, acceso["id_grupo"]])

    registrar_auditoria(
        id_tarea=tarea_id,
        accion="CAMBIAR_ESTADO",
        campo="estado",
        valor_anterior=estado_anterior,
        valor_nuevo=nuevo_estado,
        usuario=request.user.username,
        observaciones=f"Cambio de estado por {acceso['alias']}"
    )

    messages.success(request, "Estado actualizado.")
    return redirect("gestor_tareas_home")





@login_required
def detalle_tarea(request, tarea_id):
    acceso = validar_acceso_gestor(request)
    if not acceso:
        messages.error(request, "No tienes permiso o grupo asignado para Gestor de tareas.")
        return redirect("login_gestor_tareas")

    tareas = read_tasks(id_grupo=acceso["id_grupo"])

    tarea = None
    for t in tareas:
        if int(t.get("id", 0)) == int(tarea_id):
            tarea = t
            break

    if not tarea:
        messages.error(request, "Tarea no encontrada.")
        return redirect("gestor_tareas_home")

    if "prioridad" not in tarea or not tarea.get("prioridad"):
        tarea["prioridad"] = "Normal"

    if request.method == "POST":
        usuario = request.user.username

        fecha_anterior = (tarea.get("fecha") or "").strip()
        estado_anterior = (tarea.get("estado") or "").strip()
        prioridad_anterior = (tarea.get("prioridad") or "").strip()
        ambito_anterior = (tarea.get("ambito") or "").strip()
        tecnico_anterior = (tarea.get("tecnico") or "").strip()
        titulo_anterior = (tarea.get("titulo") or "").strip()
        descripcion_anterior = (tarea.get("descripcion") or "").strip()
        fecha_objetivo_anterior = (tarea.get("fecha_objetivo") or "").strip()

        fecha_nueva = request.POST.get("fecha", "").strip()
        estado_nuevo = request.POST.get("estado", "").strip()
        prioridad_nueva = request.POST.get("prioridad", "").strip() or "Normal"
        ambito_nuevo = request.POST.get("ambito", "").strip()
        tecnico_nuevo = request.POST.get("tecnico", "").strip()
        titulo_nuevo = request.POST.get("titulo", "").strip()
        descripcion_nueva = request.POST.get("descripcion", "").strip()
        fecha_objetivo_nueva = request.POST.get("fecha_objetivo", "").strip()

        tipos_alerta_ids = request.POST.getlist("tipos_alerta")
        tipos_alerta_ids = [int(x) for x in tipos_alerta_ids if x.isdigit()]

        if fecha_objetivo_nueva and not tipos_alerta_ids:
            messages.error(request, "Debes seleccionar al menos una antelación de alerta.")

            tarea["fecha"] = fecha_nueva
            tarea["estado"] = estado_nuevo
            tarea["prioridad"] = prioridad_nueva
            tarea["ambito"] = ambito_nuevo
            tarea["tecnico"] = tecnico_nuevo
            tarea["titulo"] = titulo_nuevo
            tarea["descripcion"] = descripcion_nueva
            tarea["fecha_objetivo"] = fecha_objetivo_nueva

            context = {
                "tarea": tarea,
                "estados": read_estados(),
                "ambitos": read_ambitos(),
                "tecnicos": read_tecnicos(id_grupo=acceso["id_grupo"]),
                "prioridades": PRIORIDADES,
                "tipos_alerta": read_tipos_alerta(),
                "alertas_activas": tipos_alerta_ids,
                "notas": read_notas_tarea(tarea_id),
            }
            return render(request, "gestortareas/detalle_tarea.html", context)

        tarea_model = Tarea.objects.select_related(
            "estado",
            "ambito",
            "tecnico",
            "grupo",
        ).get(
            id=tarea_id,
            grupo_id=acceso["id_grupo"],
            activa=True,
        )

        estado_obj = EstadoTarea.objects.filter(
            nombre=estado_nuevo,
            activo=True,
        ).first()

        ambito_obj = AmbitoTarea.objects.filter(
            nombre=ambito_nuevo,
            activo=True,
        ).first()

        tecnico_obj = None
        if tecnico_nuevo:
            tecnico_obj = Tecnico.objects.filter(
                nombre=tecnico_nuevo,
                activo=True,
            ).first()

        tarea_model.fecha = datetime.strptime(
            fecha_nueva,
            "%d/%m/%Y"
        ).date()

        tarea_model.estado = estado_obj
        tarea_model.prioridad = prioridad_nueva
        tarea_model.ambito = ambito_obj
        tarea_model.tecnico = tecnico_obj
        tarea_model.titulo = titulo_nuevo
        tarea_model.descripcion = descripcion_nueva

        if fecha_objetivo_nueva:
            tarea_model.fecha_objetivo = datetime.strptime(
                fecha_objetivo_nueva,
                "%Y-%m-%dT%H:%M"
            )
        else:
            tarea_model.fecha_objetivo = None

        tarea_model.save()

        guardar_alertas_tarea(tarea_id, fecha_objetivo_nueva, tipos_alerta_ids)

        cambios = [
            ("fecha", fecha_anterior, fecha_nueva),
            ("estado", estado_anterior, estado_nuevo),
            ("prioridad", prioridad_anterior, prioridad_nueva),
            ("ambito", ambito_anterior, ambito_nuevo),
            ("tecnico", tecnico_anterior, tecnico_nuevo),
            ("titulo", titulo_anterior, titulo_nuevo),
            ("descripcion", descripcion_anterior, descripcion_nueva),
            ("fecha_objetivo", fecha_objetivo_anterior, fecha_objetivo_nueva),
        ]

        for campo, valor_anterior, valor_nuevo in cambios:
            if str(valor_anterior or "") != str(valor_nuevo or ""):
                registrar_auditoria(
                    id_tarea=tarea_id,
                    accion="EDITAR",
                    campo=campo,
                    valor_anterior=str(valor_anterior or ""),
                    valor_nuevo=str(valor_nuevo or ""),
                    usuario=usuario,
                    observaciones=f"Edición desde detalle por {acceso['alias']}"
                )

        messages.success(request, "Tarea actualizada correctamente.")
        return redirect("detalle_tarea", tarea_id=tarea_id)
    
    if not tarea:
        messages.error(request, "Tarea no encontrada.")
        return redirect("gestor_tareas_home")

    tarea_model = Tarea.objects.select_related(
        "estado",
        "ambito",
        "tecnico",
        "grupo",
    ).get(
        id=tarea_id,
        grupo_id=acceso["id_grupo"],
        activa=True,
    )

    subtareas_ia = None

    if request.GET.get("generar_subtareas_ia") == "1":
        subtareas_ia = generar_subtareas_ia(tarea_model)
    
    if request.GET.get("crear_checklist_ia") == "1":

        texto_ia = generar_subtareas_ia(tarea_model)

        lineas = texto_ia.splitlines()

        creadas = 0

        for linea in lineas:

            linea = linea.strip()

            if not linea:
                continue

            if linea[0].isdigit():
                partes = linea.split(".", 1)

            if len(partes) > 1:
                linea = partes[1].strip()

            if len(linea) < 3:
                continue

            existe = Subtarea.objects.filter(
                tarea=tarea_model,
                texto=linea,
            ).exists()

            if not existe:

                Subtarea.objects.create(
                    tarea=tarea_model,
                    texto=linea,
                    completada=False,
                    creada_por_ia=True,
                )

                creadas += 1

        messages.success(
            request,
            f"Checklist IA generado ({creadas} subtareas)."
        )

        return redirect("detalle_tarea", tarea_id=tarea_id)
    
    prioridad_ia = None

    if request.GET.get("analizar_prioridad_ia") == "1":
        prioridad_ia = analizar_prioridad_ia(tarea_model)

    subtareas = (
        Subtarea.objects
            .filter(tarea_id=tarea_id)
            .order_by("completada", "id_subtarea")
    )
    print("DEBUG SUBTAREAS:", [
        (s.pk, s.id_subtarea, s.texto) for s in subtareas
    ])
    context = {
        "tarea": tarea,
        "estados": read_estados(),
        "ambitos": read_ambitos(),
        "tecnicos": read_tecnicos(id_grupo=acceso["id_grupo"]),
        "prioridades": PRIORIDADES,
        "tipos_alerta": read_tipos_alerta(),
        "alertas_activas": read_alertas_tarea(tarea_id),
        "notas": read_notas_tarea(tarea_id),
        "subtareas_ia": subtareas_ia,
        "prioridad_ia": prioridad_ia,
        "subtareas": subtareas,
    }

    return render(request, "gestortareas/detalle_tarea.html", context)


@login_required
def listado_tareas(request):
    acceso = validar_acceso_gestor(request)
    if not acceso:
        messages.error(request, "No tienes permiso o grupo asignado para Gestor de tareas.")
        return redirect("/")

    tareas = read_tasks(id_grupo=acceso["id_grupo"])

    estado_filtro = request.GET.get("estado", "").strip()
    ambito_filtro = request.GET.get("ambito", "").strip()
    tecnico_filtro = request.GET.get("tecnico", "").strip()
    fecha_filtro = request.GET.get("fecha", "").strip()
    q_raw = request.GET.get("q", "").strip()
    q = q_raw.lower()

    ordenar = request.GET.get("ordenar", "").strip()
    direccion = request.GET.get("dir", "asc").strip()

    tareas_filtradas = tareas[:]

    if estado_filtro:
        tareas_filtradas = [t for t in tareas_filtradas if t.get("estado", "") == estado_filtro]

    if ambito_filtro:
        tareas_filtradas = [t for t in tareas_filtradas if t.get("ambito", "") == ambito_filtro]

    if tecnico_filtro:
        tareas_filtradas = [t for t in tareas_filtradas if t.get("tecnico", "") == tecnico_filtro]

    if fecha_filtro:
        tareas_filtradas = [t for t in tareas_filtradas if str(t.get("fecha", "")).strip() == fecha_filtro]

    if q:
        tareas_filtradas = [
            t for t in tareas_filtradas
            if q in str(t.get("titulo", "")).lower()
            or q in str(t.get("descripcion", "")).lower()
            or q in str(t.get("estado", "")).lower()
            or q in str(t.get("ambito", "")).lower()
            or q in str(t.get("tecnico", "")).lower()
        ]

    reverse = (direccion == "desc")

    if ordenar == "fecha":
        tareas_filtradas.sort(key=lambda t: str(t.get("fecha", "")), reverse=reverse)
    elif ordenar == "estado":
        tareas_filtradas.sort(key=lambda t: str(t.get("estado", "")).lower(), reverse=reverse)
    elif ordenar == "ambito":
        tareas_filtradas.sort(key=lambda t: str(t.get("ambito", "")).lower(), reverse=reverse)
    elif ordenar == "tecnico":
        tareas_filtradas.sort(key=lambda t: str(t.get("tecnico", "")).lower(), reverse=reverse)

    context = {
        "tareas": tareas_filtradas,
        "estados": read_estados(),
        "ambitos": read_ambitos(),
        "tecnicos": read_tecnicos(id_grupo=acceso["id_grupo"]),
        "filtros": {
            "estado": estado_filtro,
            "ambito": ambito_filtro,
            "tecnico": tecnico_filtro,
            "fecha": fecha_filtro,
            "q": q_raw,
        },
        "ordenar": ordenar,
        "direccion": direccion,
        "fecha_impresion": datetime.now().strftime("%d/%m/%Y %H:%M"),
        "total_tareas": len(tareas_filtradas),
    }

    return render(request, "gestortareas/listado_tareas.html", context)


@login_required
@require_POST
def nuevo_ambito(request):
    acceso = validar_acceso_gestor(request)
    if not acceso:
        messages.error(request, "No tienes permiso o grupo asignado para Gestor de tareas.")
        return redirect("/")

    nombre = request.POST.get("nuevo_ambito", "").strip()
    if not nombre:
        messages.error(request, "Debes indicar un ámbito.")
        return redirect("gestor_tareas_home")

    sql = """
        INSERT INTO gestor_tareas_tbambitos (nombre, activo)
        VALUES (%s, 1)
        ON DUPLICATE KEY UPDATE activo = VALUES(activo)
    """

    with connection.cursor() as cursor:
        cursor.execute(sql, [nombre])

    messages.success(request, "Ámbito guardado.")
    return redirect("gestor_tareas_home")


@login_required
@require_POST
def nuevo_tecnico(request):
    acceso = validar_acceso_gestor(request)
    if not acceso:
        messages.error(request, "No tienes permiso o grupo asignado para Gestor de tareas.")
        return redirect("login_gestor_tareas")

    nombre = request.POST.get("nuevo_tecnico", "").strip()
    if not nombre:
        messages.error(request, "Debes indicar un técnico.")
        return redirect("gestor_tareas_home")

    with connection.cursor() as cursor:
        cursor.execute("""
            INSERT INTO gestor_tareas_tbtecnicos (nombre, activo)
            VALUES (%s, 1)
            ON DUPLICATE KEY UPDATE activo = VALUES(activo)
        """, [nombre])

        cursor.execute("""
            SELECT id_tecnico
            FROM gestor_tareas_tbtecnicos
            WHERE nombre = %s
            LIMIT 1
        """, [nombre])
        row = cursor.fetchone()

        if row:
            id_tecnico = row[0]

            cursor.execute("""
                INSERT INTO gestor_tareas_tbtecnicos_grupos (id_tecnico, id_grupo, activo)
                VALUES (%s, %s, 1)
                ON DUPLICATE KEY UPDATE activo = VALUES(activo)
            """, [id_tecnico, acceso["id_grupo"]])

    messages.success(request, "Técnico guardado y vinculado al grupo.")
    return redirect("gestor_tareas_home")



def cambiar_grupo(request):
    nuevo_grupo = request.POST.get("grupo")

    request.session["gestor_tareas_id_grupo"] = int(nuevo_grupo)

    return redirect("gestor_tareas_home")

