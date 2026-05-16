from __future__ import annotations

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.db import connection
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST
from datetime import datetime, timedelta
from .models import (
    UsuarioGestor,
    UsuarioGrupo,
    Tarea,
    EstadoTarea,
    AmbitoTarea,
    Tecnico,
    GrupoTrabajo,
)
from django.http import HttpResponse
from django.template.loader import render_to_string


# =========================================================
# Constantes
# =========================================================

# Pon aquí el ID real de la actuación del gestor
ID_ACTUACION_GESTOR_TAREAS = 908
PRIORIDADES = ["Baja", "Normal", "Alta", "Urgente"]


# =========================================================
# Permisos / acceso
# =========================================================

def login_gestor_tareas(request):
    """
    Login local del módulo Gestor de tareas.
    Usa usuarios estándar de Django.
    """
    if request.method == "POST":
        username = request.POST.get("usuario", "").strip()
        password = request.POST.get("password", "").strip()

        if not username or not password:
            messages.error(request, "Debes indicar usuario y contraseña.")
            return render(request, "gestortareas/login.html")

        user = authenticate(request, username=username, password=password)

        if user is None:
            messages.error(request, "Usuario o contraseña incorrectos.")
            return render(request, "gestortareas/login.html")

        login(request, user)

        acceso = validar_acceso_gestor(request)
        if not acceso:
            messages.error(request, "Tu usuario no tiene acceso al Gestor de tareas.")
            return render(request, "gestortareas/login.html")

        return redirect("gestor_tareas_home")

    return render(request, "gestortareas/login.html")


# =========================================================
# Catálogos desde BD
# =========================================================

def read_estados():
    sql = """
        SELECT nombre
        FROM gestor_tareas_tbestados
        WHERE activo = 1
        ORDER BY orden, nombre
    """
    with connection.cursor() as cursor:
        cursor.execute(sql)
        return [row[0] for row in cursor.fetchall()]


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
    estados = read_estados()
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

    total_tareas = len(tareas)
    
    total_pendientes = sum(1 for t in tareas if t.get("estado") == "Pendiente")
    total_pendientes_firma = sum(1 for t in tareas if t.get("estado") == "Pte. de firma")
    total_programadas = sum(1 for t in tareas if t.get("estado") == "Programada")
    total_urgentes = sum(1 for t in tareas if t.get("estado") == "Urgente")
    total_completadas = sum(1 for t in tareas if t.get("estado") == "Completada")
    alertas_pendientes = read_alertas_pendientes_para_grupo(id_grupo)
    total_pendientes_devolucion = sum(    1 for t in tareas if t.get("estado") == "Pte. devolución")

# DEBUB PARA ELIMINAR INICIO
    #print("DEBUG filtros =", filtros)
    #print("DEBUG num tareas filtradas =", len(tareas_filtradas))
# DEBUB PARA ELIMINAR FIN
    context = {
        "tareas": tareas_filtradas,
        "estados": estados,
        "ambitos": ambitos,
        "tecnicos": tecnicos,
        "filtros": filtros,
        "usuario_alias": acceso["alias"],
        "total_tareas": total_tareas,
        "total_pendientes": total_pendientes,
        "total_pendientes_firma": total_pendientes_firma,
        "total_programadas": total_programadas,
        "total_urgentes": total_urgentes,
        "total_completadas": total_completadas,
        "total_pendientes_devolucion": total_pendientes_devolucion,
        "alertas_pendientes": alertas_pendientes,
        "grupos_usuario": grupos_usuario,
        "grupo_activo": acceso["id_grupo"],
        "grupo_activo_nombre": acceso["grupo"],
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
        (id_tarea, usuario, texto)
        VALUES (%s, %s, %s)
    """

    with connection.cursor() as cursor:
        cursor.execute(sql, [id_tarea, usuario, texto])

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
        "estados": read_estados(),
        "ambitos": read_ambitos(),
        "tecnicos": read_tecnicos(id_grupo=acceso["id_grupo"]),
        "prioridades": PRIORIDADES,
        "hoy": datetime.now().strftime("%d/%m/%Y"),
    }

    return render(request, "gestortareas/nueva_tarea.html", context)

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

        with connection.cursor() as cursor:
            # Resolver id_estado
            cursor.execute("""
                SELECT id_estado
                FROM gestor_tareas_tbestados
                WHERE nombre = %s
                LIMIT 1
            """, [estado_nuevo])
            row = cursor.fetchone()
            id_estado_nuevo = row[0] if row else None

            # Resolver id_ambito
            cursor.execute("""
                SELECT id_ambito
                FROM gestor_tareas_tbambitos
                WHERE nombre = %s
                LIMIT 1
            """, [ambito_nuevo])
            row = cursor.fetchone()
            id_ambito_nuevo = row[0] if row else None

            # Resolver id_tecnico
            id_tecnico_nuevo = None
            if tecnico_nuevo:
                cursor.execute("""
                    SELECT id_tecnico
                    FROM gestor_tareas_tbtecnicos
                    WHERE nombre = %s
                    LIMIT 1
                """, [tecnico_nuevo])
                row = cursor.fetchone()
                id_tecnico_nuevo = row[0] if row else None

            sql_update = """
                UPDATE gestor_tareas_tbtareas
                SET
                    fecha = STR_TO_DATE(%s, '%%d/%%m/%%Y'),
                    id_estado = %s,
                    prioridad = %s,
                    id_ambito = %s,
                    id_tecnico = %s,
                    titulo = %s,
                    descripcion = %s,
                    fecha_objetivo = CASE
                        WHEN %s = '' THEN NULL
                        ELSE STR_TO_DATE(%s, '%%Y-%%m-%%dT%%H:%%i')
                    END
                WHERE id = %s
                  AND id_grupo = %s
            """

            cursor.execute(sql_update, [
                fecha_nueva,
                id_estado_nuevo,
                prioridad_nueva,
                id_ambito_nuevo,
                id_tecnico_nuevo,
                titulo_nuevo,
                descripcion_nueva,
                fecha_objetivo_nueva,
                fecha_objetivo_nueva,
                tarea_id,
                acceso["id_grupo"],
            ])

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

    context = {
        "tarea": tarea,
        "estados": read_estados(),
        "ambitos": read_ambitos(),
        "tecnicos": read_tecnicos(id_grupo=acceso["id_grupo"]),
        "prioridades": PRIORIDADES,
        "tipos_alerta": read_tipos_alerta(),
        "alertas_activas": read_alertas_tarea(tarea_id),
        "notas": read_notas_tarea(tarea_id),
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

def cambiar_grupo(request):
    nuevo_grupo = request.POST.get("grupo")

    request.session["gestor_tareas_id_grupo"] = int(nuevo_grupo)

    return redirect("gestor_tareas_home")

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