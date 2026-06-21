import random

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from praktiko.forms.practica_forms import ConfiguracionPracticaForm
from praktiko.models import EntradaDiccionario, RespuestaPractica, SesionPractica


@login_required
def configurar_practica(request):
    if request.method == "POST":
        form = ConfiguracionPracticaForm(request.POST, usuario=request.user)

        if form.is_valid():
            diccionario = form.cleaned_data["diccionario"]
            tema = form.cleaned_data["tema"]
            numero_preguntas = form.cleaned_data["numero_preguntas"]
            modo = form.cleaned_data["modo"]

            entradas = EntradaDiccionario.objects.filter(
                usuario=request.user,
                diccionario=diccionario,
                activa=True,
            )

            if tema:
                entradas = entradas.filter(tema=tema)

            if modo == SesionPractica.MODO_DIFICILES:
                entradas = [
                    entrada for entrada in entradas
                    if entrada.es_dificil
                ]

            elif modo == SesionPractica.MODO_FALLADAS:
                entradas = entradas.filter(veces_fallada__gt=0)

            else:
                entradas = list(entradas)

            if len(entradas) < 2:
                messages.error(
                    request,
                    "Necesitas al menos 2 entradas activas para iniciar una práctica.",
                )
                return redirect("praktiko:configurar_practica")

            random.shuffle(entradas)
            entradas_seleccionadas = entradas[:numero_preguntas]

            sesion = SesionPractica.objects.create(
                usuario=request.user,
                diccionario=diccionario,
                tema=tema,
                modo=modo,
                total_tarjetas=len(entradas_seleccionadas),
                aciertos=0,
                fallos=0,
            )

            request.session["praktiko_sesion_id"] = sesion.id
            request.session["praktiko_entradas_ids"] = [
                entrada.id for entrada in entradas_seleccionadas
            ]
            request.session["praktiko_indice_actual"] = 0
            request.session["praktiko_mostrar_respuesta"] = False
            request.session["praktiko_falladas_ids"] = []

            return redirect("praktiko:pregunta_practica")
    else:
        form = ConfiguracionPracticaForm(usuario=request.user)

    return render(
        request,
        "praktiko/practica/configurar.html",
        {
            "form": form,
        },
    )


@login_required
def pregunta_practica(request):
    sesion_id = request.session.get("praktiko_sesion_id")
    entradas_ids = request.session.get("praktiko_entradas_ids", [])
    indice_actual = request.session.get("praktiko_indice_actual", 0)

    if not sesion_id or not entradas_ids:
        messages.error(request, "No hay ninguna práctica activa.")
        return redirect("praktiko:configurar_practica")

    if request.method == "POST":
        accion = request.POST.get("accion")

        if accion == "mostrar":
            request.session["praktiko_mostrar_respuesta"] = True
            return redirect("praktiko:pregunta_practica")

        if accion in ["error", "dificil", "correcto", "facil"]:
            sesion = get_object_or_404(
                SesionPractica,
                id=sesion_id,
                usuario=request.user,
            )

            entrada_id = entradas_ids[indice_actual]
            entrada = get_object_or_404(
                EntradaDiccionario,
                id=entrada_id,
                usuario=request.user,
            )

            correcta = accion in ["dificil", "correcto", "facil"]

            RespuestaPractica.objects.create(
                sesion=sesion,
                entrada=entrada,
                texto_origen=entrada.texto_origen,
                respuesta_elegida=accion,
                respuesta_correcta=entrada.texto_destino,
                correcta=correcta,
                evaluacion=accion,
            )

            entrada.registrar_respuesta(correcta)

            if correcta:
                sesion.aciertos += 1
            else:
                sesion.fallos += 1

                falladas_ids = request.session.get("praktiko_falladas_ids", [])
                falladas_ids.append(entrada.id)
                request.session["praktiko_falladas_ids"] = falladas_ids

            sesion.save(update_fields=["aciertos", "fallos"])

            request.session["praktiko_mostrar_respuesta"] = False
            request.session["praktiko_indice_actual"] = indice_actual + 1

            return redirect("praktiko:pregunta_practica")

    if indice_actual >= len(entradas_ids):
        return redirect("praktiko:resultado_practica")

    entrada_id = entradas_ids[indice_actual]

    entrada = EntradaDiccionario.objects.get(
        id=entrada_id,
        usuario=request.user,
    )

    mostrar_respuesta = request.session.get(
        "praktiko_mostrar_respuesta",
        False,
    )
    
    return render(
        request,
        "praktiko/practica/pregunta.html",
        {
            "entrada": entrada,
            "indice_actual": indice_actual + 1,
            "total": len(entradas_ids),
            "mostrar_respuesta": mostrar_respuesta,
            "modo_practica": True,
        },
    )

@login_required
def resultado_practica(request):
    sesion_id = request.session.get("praktiko_sesion_id")
    falladas_ids = request.session.get("praktiko_falladas_ids", [])

    sesion = get_object_or_404(
        SesionPractica,
        id=sesion_id,
        usuario=request.user,
    )

    sesion.finalizar()

    falladas = EntradaDiccionario.objects.filter(
        id__in=falladas_ids,
        usuario=request.user,
    )

    contexto = {
        "sesion": sesion,
        "falladas": falladas,
    }

    request.session.pop("praktiko_sesion_id", None)
    request.session.pop("praktiko_entradas_ids", None)
    request.session.pop("praktiko_indice_actual", None)
    request.session.pop("praktiko_falladas_ids", None)
    request.session.pop("praktiko_mostrar_respuesta", None)

    return render(
        request,
        "praktiko/practica/resultado.html",
        contexto,
    )