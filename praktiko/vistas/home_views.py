from django.contrib.auth.decorators import login_required
from django.db.models import Count, Sum
from django.shortcuts import render

from praktiko.models import (
    Diccionario,
    Tema,
    EntradaDiccionario,
    SesionPractica,
    InvitacionGrupoAprendizaje,
    EstadisticaEntradaUsuario,
)


@login_required
def home(request):
    usuario = request.user

    total_diccionarios = Diccionario.objects.filter(usuario=usuario).count()
    total_temas = Tema.objects.filter(usuario=usuario).count()
    total_entradas = EntradaDiccionario.objects.filter(usuario=usuario).count()
    total_sesiones = SesionPractica.objects.filter(usuario=usuario).count()
    invitaciones_pendientes = InvitacionGrupoAprendizaje.objects.filter(
        invitado=usuario,
        estado=InvitacionGrupoAprendizaje.ESTADO_PENDIENTE,
    ).count()
    resumen_sesiones = SesionPractica.objects.filter(usuario=usuario).aggregate(
        total_aciertos=Sum("aciertos"),
        total_fallos=Sum("fallos"),
        total_tarjetas=Sum("total_tarjetas"),
    )

    total_aciertos = resumen_sesiones["total_aciertos"] or 0
    total_fallos = resumen_sesiones["total_fallos"] or 0
    total_tarjetas = resumen_sesiones["total_tarjetas"] or 0

    if total_tarjetas > 0:
        porcentaje_acierto = round((total_aciertos / total_tarjetas) * 100, 2)
    else:
        porcentaje_acierto = 0

    estadisticas_dificiles_qs = (
        EstadisticaEntradaUsuario.objects
        .filter(
            usuario=usuario,
            veces_preguntada__gte=3,
        )
        .select_related("entrada")
    )

    total_palabras_dificiles = sum(
        1
        for estadistica in estadisticas_dificiles_qs
        if estadistica.porcentaje_acierto < 60
    )

    diccionarios = (
        Diccionario.objects
        .filter(usuario=usuario, activo=True)
        .annotate(
            total_temas=Count("temas", distinct=True),
            total_entradas=Count("entradas", distinct=True),
        )
        .order_by("nombre")
    )

    contexto = {
        "total_diccionarios": total_diccionarios,
        "total_temas": total_temas,
        "total_entradas": total_entradas,
        "total_sesiones": total_sesiones,
        "total_aciertos": total_aciertos,
        "total_fallos": total_fallos,
        "porcentaje_acierto": porcentaje_acierto,
        "diccionarios": diccionarios,
        "invitaciones_pendientes": invitaciones_pendientes,
        "total_palabras_dificiles": total_palabras_dificiles,
    }

    return render(request, "praktiko/home.html", contexto)