from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.translation import gettext as _

from praktiko.forms.examen_forms import ConfiguracionExamenForm
from praktiko.models import EntradaDiccionario, Examen, RespuestaExamen
from praktiko.servicios.examen_service import (
    calificacion_examen,
    preparar_preguntas_examen,
    respuesta_es_correcta,
    seleccionar_entradas_examen,
)


CLAVE_EXAMEN_ID = "praktiko_examen_id"
CLAVE_PREGUNTAS = "praktiko_examen_preguntas"
CLAVE_INDICE = "praktiko_examen_indice"


def _limpiar_sesion_examen(request):
    request.session.pop(CLAVE_EXAMEN_ID, None)
    request.session.pop(CLAVE_PREGUNTAS, None)
    request.session.pop(CLAVE_INDICE, None)


@login_required
def configurar_examen(request):
    if request.method == "POST":
        form = ConfiguracionExamenForm(
            request.POST,
            usuario=request.user,
        )

        if form.is_valid():
            diccionario = form.cleaned_data["diccionario"]
            tema = form.cleaned_data["tema"]
            numero_preguntas = form.cleaned_data["numero_preguntas"]
            sentido = form.cleaned_data["sentido"]

            entradas = seleccionar_entradas_examen(
                usuario=request.user,
                diccionario=diccionario,
                tema=tema,
                numero_preguntas=numero_preguntas,
            )

            if not entradas:
                messages.error(
                    request,
                    _(
                        "No hay suficientes entradas activas para preparar "
                        "un examen de %(numero)s preguntas."
                    )
                    % {"numero": numero_preguntas},
                )
                return redirect("praktiko:examen_configurar")

            preguntas = preparar_preguntas_examen(
                entradas,
                sentido,
            )

            _limpiar_sesion_examen(request)

            examen = Examen.objects.create(
                usuario=request.user,
                diccionario=diccionario,
                tema=tema,
                tipo=Examen.TIPO_NORMAL,
                sentido=sentido,
                numero_preguntas=len(preguntas),
                estado=Examen.ESTADO_EN_CURSO,
            )

            request.session[CLAVE_EXAMEN_ID] = examen.id
            request.session[CLAVE_PREGUNTAS] = preguntas
            request.session[CLAVE_INDICE] = 0

            return redirect("praktiko:examen_pregunta")
    else:
        form = ConfiguracionExamenForm(usuario=request.user)

    return render(
        request,
        "praktiko/examen/configurar.html",
        {"form": form},
    )


@login_required
def pregunta_examen(request):
    examen_id = request.session.get(CLAVE_EXAMEN_ID)
    preguntas = request.session.get(CLAVE_PREGUNTAS, [])
    indice = request.session.get(CLAVE_INDICE, 0)

    if not examen_id or not preguntas:
        messages.error(request, _("No hay ningún examen activo."))
        return redirect("praktiko:examen_configurar")

    examen = get_object_or_404(
        Examen,
        id=examen_id,
        usuario=request.user,
        estado=Examen.ESTADO_EN_CURSO,
    )

    if indice >= len(preguntas):
        return redirect("praktiko:examen_resultado")

    pregunta = preguntas[indice]

    if request.method == "POST":
        respuesta_usuario = request.POST.get("respuesta", "").strip()

        if not respuesta_usuario:
            messages.error(request, _("Debes escribir una respuesta."))
            return redirect("praktiko:examen_pregunta")

        entrada = get_object_or_404(
            EntradaDiccionario,
            id=pregunta["entrada_id"],
            usuario=request.user,
        )

        correcta = respuesta_es_correcta(
            respuesta_usuario,
            pregunta["respuesta_correcta"],
        )

        with transaction.atomic():
            RespuestaExamen.objects.create(
                examen=examen,
                entrada=entrada,
                tema_id=pregunta["tema_id"],
                sentido=pregunta["sentido"],
                texto_pregunta=pregunta["texto_pregunta"],
                respuesta_usuario=respuesta_usuario,
                respuesta_correcta=pregunta["respuesta_correcta"],
                correcta=correcta,
                orden=pregunta["orden"],
            )

            request.session[CLAVE_INDICE] = indice + 1

        return redirect("praktiko:examen_pregunta")

    return render(
        request,
        "praktiko/examen/pregunta.html",
        {
            "examen": examen,
            "pregunta": pregunta,
            "numero_actual": indice + 1,
            "total": len(preguntas),
        },
    )


@login_required
def resultado_examen(request):
    examen_id = request.session.get(CLAVE_EXAMEN_ID)

    if not examen_id:
        messages.error(request, _("No se ha encontrado el examen."))
        return redirect("praktiko:examen_configurar")

    examen = get_object_or_404(
        Examen,
        id=examen_id,
        usuario=request.user,
    )

    if examen.estado == Examen.ESTADO_EN_CURSO:
        examen.finalizar()

    respuestas = examen.respuestas.select_related("tema").all()

    temas = {}
    for respuesta in respuestas:
        nombre_tema = (
            respuesta.tema.nombre
            if respuesta.tema
            else _("Sin tema")
        )
        datos = temas.setdefault(
            nombre_tema,
            {"total": 0, "aciertos": 0},
        )
        datos["total"] += 1
        if respuesta.correcta:
            datos["aciertos"] += 1

    desglose_temas = []
    for nombre, datos in temas.items():
        porcentaje = round(
            (datos["aciertos"] / datos["total"]) * 100,
            2,
        )
        desglose_temas.append(
            {
                "nombre": nombre,
                "total": datos["total"],
                "aciertos": datos["aciertos"],
                "porcentaje": porcentaje,
            }
        )

    desglose_temas.sort(
        key=lambda elemento: (
            elemento["porcentaje"],
            elemento["nombre"],
        )
    )

    _limpiar_sesion_examen(request)

    return render(
        request,
        "praktiko/examen/resultado.html",
        {
            "examen": examen,
            "respuestas": respuestas,
            "desglose_temas": desglose_temas,
            "calificacion": calificacion_examen(float(examen.nota)),
        },
    )
