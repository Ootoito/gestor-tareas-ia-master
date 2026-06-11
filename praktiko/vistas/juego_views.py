import random
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from praktiko.models import Diccionario, Tema, EntradaDiccionario
from django.contrib import messages



@login_required
def configurar_juego(request):

    diccionarios = (
        Diccionario.objects
        .filter(usuario=request.user)
        .order_by("nombre")
    )

    temas = (
        Tema.objects
        .filter(diccionario__usuario=request.user)
        .order_by("orden", "nombre")
    )

    return render(
        request,
        "praktiko/juego/configurar.html",
        {
            "diccionarios": diccionarios,
            "temas": temas,
        },
    )

@login_required
def tablero_juego(request):
    if request.GET.get("diccionario"):
        request.session["juego_diccionario_id"] = request.GET.get("diccionario")

    if request.GET.get("tema"):
        request.session["juego_tema_id"] = request.GET.get("tema")

    if request.GET.get("fichas"):
        request.session["juego_numero_fichas"] = int(request.GET.get("fichas"))
        request.session["juego_fichas_eliminadas"] = []
        request.session["juego_puntos"] = 0
        request.session["juego_aciertos"] = 0
        request.session["juego_errores"] = 0

    numero_fichas = request.session.get("juego_numero_fichas", 12)
    fichas = list(range(1, numero_fichas + 1))

    eliminadas = request.session.get("juego_fichas_eliminadas", [])
    puntos = request.session.get("juego_puntos", 0)
    aciertos = request.session.get("juego_aciertos", 0)
    errores = request.session.get("juego_errores", 0)

    restantes = numero_fichas - len(eliminadas)

    if restantes <= 0:
        return redirect("praktiko:juego_resultado")

    return render(
        request,
        "praktiko/juego/tablero.html",
        {
            "fichas": fichas,
            "eliminadas": eliminadas,
            "puntos": puntos,
            "aciertos": aciertos,
            "errores": errores,
            "restantes": restantes,
        },
    )

@login_required
def pregunta_juego(request):
    diccionario_id = request.session.get("juego_diccionario_id")
    tema_id = request.session.get("juego_tema_id")
    ficha = request.GET.get("ficha") or request.POST.get("ficha")
    
    if request.method == "POST":
        entrada_correcta_id = request.POST.get("entrada_correcta_id")
        respuesta_id = request.POST.get("respuesta_id")

        if entrada_correcta_id == respuesta_id:
            eliminadas = request.session.get("juego_fichas_eliminadas", [])

            if ficha and ficha not in eliminadas:
                eliminadas.append(ficha)

            puntos = request.session.get("juego_puntos", 0)
            aciertos = request.session.get("juego_aciertos", 0)

            request.session["juego_fichas_eliminadas"] = eliminadas
            request.session["juego_puntos"] = puntos + 100
            request.session["juego_aciertos"] = aciertos + 1

            messages.success(request, "¡Correcto! Ficha eliminada. +100 puntos.")
        else:
            errores = request.session.get("juego_errores", 0)
            request.session["juego_errores"] = errores + 1

            messages.error(request, "Respuesta incorrecta. La ficha vuelve al tablero.")

        return redirect("praktiko:juego_tablero")

    entradas = EntradaDiccionario.objects.filter(
        usuario=request.user,
        diccionario_id=diccionario_id,
        activa=True,
    )

    if tema_id:
        entradas = entradas.filter(tema_id=tema_id)

    entradas = list(entradas)

    if len(entradas) < 3:
        messages.error(
            request,
            "Necesitas al menos 3 entradas activas para jugar.",
        )
        return redirect("praktiko:juego_configurar")

    entrada_correcta = random.choice(entradas)

    incorrectas = [
        entrada for entrada in entradas
        if entrada.id != entrada_correcta.id
    ]

    opciones = random.sample(incorrectas, 2)
    opciones.append(entrada_correcta)
    random.shuffle(opciones)
    
    return render(
        request,
        "praktiko/juego/pregunta.html",
        {
            "entrada": entrada_correcta,
            "opciones": opciones,
            "ficha": ficha,
        },
    )

@login_required
def resultado_juego(request):
    puntos = request.session.get("juego_puntos", 0)
    aciertos = request.session.get("juego_aciertos", 0)
    errores = request.session.get("juego_errores", 0)
    numero_fichas = request.session.get("juego_numero_fichas", 0)

    contexto = {
        "puntos": puntos,
        "aciertos": aciertos,
        "errores": errores,
        "numero_fichas": numero_fichas,
    }

    request.session.pop("juego_diccionario_id", None)
    request.session.pop("juego_tema_id", None)
    request.session.pop("juego_numero_fichas", None)
    request.session.pop("juego_fichas_eliminadas", None)
    request.session.pop("juego_puntos", None)
    request.session.pop("juego_aciertos", None)
    request.session.pop("juego_errores", None)

    return render(
        request,
        "praktiko/juego/resultado.html",
        contexto,
    )