import random
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from praktiko.models import EstadisticaEntradaUsuario


@login_required
def mis_estadisticas(request):
    estadisticas = (
        EstadisticaEntradaUsuario.objects
        .filter(usuario=request.user)
        .select_related(
            "entrada",
            "entrada__diccionario",
            "entrada__tema",
        )
        .order_by(
            "-fallos",
            "-veces_preguntada",
        )
    )

    return render(
        request,
        "praktiko/estadisticas/mis_estadisticas.html",
        {
            "estadisticas": estadisticas,
        },
    )

@login_required
def palabras_dificiles(request):
    estadisticas = (
        EstadisticaEntradaUsuario.objects
        .filter(
            usuario=request.user,
            veces_preguntada__gte=3,
        )
        .select_related(
            "entrada",
            "entrada__diccionario",
            "entrada__tema",
        )
        .order_by(
            "-fallos",
            "-veces_preguntada",
        )
    )

    estadisticas = [
        e
        for e in estadisticas
        if e.porcentaje_acierto < 60
    ]

    return render(
        request,
        "praktiko/estadisticas/palabras_dificiles.html",
        {
            "estadisticas": estadisticas,
        },
    )

@login_required
def repasar_dificiles(request):
    estadisticas = (
        EstadisticaEntradaUsuario.objects
        .filter(
            usuario=request.user,
            veces_preguntada__gte=3,
        )
        .select_related(
            "entrada",
            "entrada__tema",
            "entrada__diccionario",
        )
        .order_by(
            "-fallos",
            "-veces_preguntada",
        )
    )

    estadisticas = [
        e
        for e in estadisticas
        if e.porcentaje_acierto < 60
    ]

    return render(
        request,
        "praktiko/estadisticas/repasar_dificiles.html",
        {
            "estadisticas": estadisticas,
        },
    )

@login_required
def jugar_dificiles(request):
    estadisticas = (
        EstadisticaEntradaUsuario.objects
        .filter(
            usuario=request.user,
            veces_preguntada__gte=3,
        )
        .select_related("entrada")
        .order_by("-fallos", "-veces_preguntada")
    )

    entradas_ids = [
        e.entrada_id
        for e in estadisticas
        if e.porcentaje_acierto < 60
    ]

    if len(entradas_ids) < 3:
        messages.error(
            request,
            "Necesitas al menos 3 palabras difíciles para iniciar este modo.",
        )
        return redirect("praktiko:palabras_dificiles")

    numero_fichas = min(len(entradas_ids), 12)

    random.shuffle(entradas_ids)

    request.session["juego_diccionario_id"] = None
    request.session["juego_tema_id"] = None
    request.session["juego_grupo_id"] = None
    request.session["juego_numero_fichas"] = numero_fichas
    request.session["juego_fichas_eliminadas"] = []
    request.session["juego_puntos"] = 0
    request.session["juego_aciertos"] = 0
    request.session["juego_errores"] = 0
    request.session["juego_entradas_ids"] = entradas_ids[:numero_fichas]
    request.session["juego_modo"] = "dificiles"

    return redirect("praktiko:juego_tablero")