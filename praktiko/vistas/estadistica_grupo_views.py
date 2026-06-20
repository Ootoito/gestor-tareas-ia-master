from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render

from praktiko.models import (
    GrupoAprendizaje,
    MiembroGrupoAprendizaje,
    EstadisticaEntradaUsuario,
)


@login_required
def estadisticas_grupo(request, grupo_id):

    grupo = get_object_or_404(
        GrupoAprendizaje,
        id=grupo_id,
    )

    miembros = (
        MiembroGrupoAprendizaje.objects
        .filter(grupo=grupo, activo=True)
        .select_related("usuario")
        .order_by("usuario__username")
    )

    resumen_miembros = []

    for miembro in miembros:

        estadisticas = EstadisticaEntradaUsuario.objects.filter(
            usuario=miembro.usuario
        )

        total_preguntas = sum(
            e.veces_preguntada
            for e in estadisticas
        )

        total_aciertos = sum(
            e.aciertos
            for e in estadisticas
        )

        total_fallos = sum(
            e.fallos
            for e in estadisticas
        )

        porcentaje = 0

        if total_preguntas > 0:
            porcentaje = round(
                (total_aciertos / total_preguntas) * 100,
                2,
            )

        resumen_miembros.append(
            {
                "usuario": miembro.usuario,
                "preguntas": total_preguntas,
                "aciertos": total_aciertos,
                "fallos": total_fallos,
                "porcentaje": porcentaje,
            }
        )

    resumen_miembros.sort(
        key=lambda x: x["porcentaje"],
        reverse=True,
    )

    return render(
        request,
        "praktiko/grupos/estadisticas_grupo.html",
        {
            "grupo": grupo,
            "resumen_miembros": resumen_miembros,
        },
    )