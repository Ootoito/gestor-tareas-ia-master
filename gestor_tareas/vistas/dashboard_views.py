# *********************************************************************
# ******************* INTELIGENCIA ARTIFICIAL - CHATGPT ************************
# *********************************************************************
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.shortcuts import redirect, render
from django.utils import timezone

from gestor_tareas.models import Tarea
from gestor_tareas.services.ia import generar_resumen_ia_gestor
from gestor_tareas.vistas.common import validar_acceso_gestor

@login_required
def dashboard_gestor(request):
    acceso = validar_acceso_gestor(request)

    import os
    print("OPENAI_API_KEY:", os.environ.get("OPENAI_API_KEY"))

    if not acceso:
        messages.error(request, "No tienes permiso o grupo asignado para Gestor de tareas.")
        return redirect("login_gestor_tareas")

    queryset = Tarea.objects.filter(
        activa=True,
        grupo_id=acceso["id_grupo"],
    )
    
    tareas_por_tecnico = (
        queryset
        .values("tecnico__nombre")
        .annotate(total=Count("id"))
        .order_by("-total")
    )
    
    datos_dashboard = {
        "grupo": acceso["grupo"],
        "total_tareas": queryset.count(),
        "total_pendientes": queryset.filter(estado__nombre="Pendiente").count(),
        "total_pendientes_firma": queryset.filter(estado__nombre="Pendiente de firma").count(),
        "total_pendientes_devolucion": queryset.filter(estado__nombre="Pendiente de devolución").count(),
        "total_programadas": queryset.filter(estado__nombre="Programada").count(),
        "total_urgentes": queryset.filter(estado__nombre="Urgente").count(),
        "total_completadas": queryset.filter(estado__nombre="Completada").count(),
        "tareas_por_tecnico": list(tareas_por_tecnico),
    }

    resumen_ia = None

    if request.GET.get("generar_ia") == "1":
        resumen_ia = generar_resumen_ia_gestor(datos_dashboard)

    analisis_ia = generar_analisis_inteligente_grupo(queryset)

    context = {
        "grupo_activo_nombre": acceso["grupo"],
        "total_tareas": queryset.count(),
        "total_pendientes": queryset.filter(estado__nombre="Pendiente").count(),
        "total_pendientes_firma": queryset.filter(estado__nombre="Pendiente de firma").count(),
        "total_pendientes_devolucion": queryset.filter(estado__nombre="Pendiente de devolución").count(),
        "total_programadas": queryset.filter(estado__nombre="Programada").count(),
        "total_completadas": queryset.filter(estado__nombre="Completada").count(),
        "total_urgentes": queryset.filter(estado__nombre="Urgente").count(),
        "tareas_por_tecnico": tareas_por_tecnico,
        "analisis_ia": analisis_ia,
        "resumen_ia": resumen_ia,
    }

    return render(request, "gestortareas/dashboard_gestor.html", context)


def generar_analisis_inteligente_grupo(queryset):
    total = queryset.count()
    pendientes = queryset.filter(estado__nombre__icontains="Pendiente").count()
    urgentes = queryset.filter(estado__nombre="Urgente").count()
    completadas = queryset.filter(estado__nombre="Completada").count()

    vencidas = queryset.filter(
        fecha_objetivo__lt=timezone.now()
    ).exclude(
        estado__nombre="Completada"
    ).count()

    tecnico_top = (
        queryset
        .values("tecnico__nombre")
        .annotate(total=Count("id"))
        .order_by("-total")
        .first()
    )

    mensajes = []

    if total == 0:
        mensajes.append("No hay tareas registradas en el grupo. Es un buen momento para planificar el trabajo inicial.")
        return mensajes

    if pendientes > 0:
        mensajes.append(f"Hay {pendientes} tareas pendientes. Conviene revisar prioridades y fechas objetivo.")

    if urgentes > 0:
        mensajes.append(f"Hay {urgentes} tareas urgentes activas. Se recomienda atenderlas antes de crear nuevas tareas.")

    if vencidas > 0:
        mensajes.append(f"Hay {vencidas} tareas vencidas según su fecha objetivo. Es recomendable revisarlas hoy.")

    if completadas == 0 and total > 0:
        mensajes.append("Todavía no hay tareas completadas. El grupo está en fase de trabajo abierto.")

    if tecnico_top and tecnico_top["tecnico__nombre"]:
        porcentaje = round((tecnico_top["total"] / total) * 100, 1)
        if porcentaje >= 50:
            mensajes.append(
                f"{tecnico_top['tecnico__nombre']} concentra el {porcentaje}% de las tareas. Puede existir sobrecarga."
            )
        else:
            mensajes.append(
                f"La carga parece repartida. El técnico con más tareas es {tecnico_top['tecnico__nombre']} con {tecnico_top['total']}."
            )

    return mensajes