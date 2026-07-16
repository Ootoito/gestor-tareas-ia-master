import random
import unicodedata

from praktiko.models import EntradaDiccionario, Examen


def seleccionar_entradas_examen(
    *,
    usuario,
    diccionario,
    tema=None,
    numero_preguntas=15,
):
    entradas = EntradaDiccionario.objects.filter(
        usuario=usuario,
        diccionario=diccionario,
        activa=True,
    )

    if tema:
        entradas = entradas.filter(tema=tema)

    entradas = list(entradas.select_related("tema"))

    if len(entradas) < numero_preguntas:
        return []

    random.shuffle(entradas)
    return entradas[:numero_preguntas]


def preparar_preguntas_examen(entradas, sentido):
    preguntas = []

    for orden, entrada in enumerate(entradas, start=1):
        sentido_pregunta = sentido

        if sentido == Examen.SENTIDO_MIXTO:
            sentido_pregunta = random.choice(
                [
                    Examen.SENTIDO_ORIGEN_DESTINO,
                    Examen.SENTIDO_DESTINO_ORIGEN,
                ]
            )

        if sentido_pregunta == Examen.SENTIDO_ORIGEN_DESTINO:
            texto_pregunta = entrada.texto_origen
            respuesta_correcta = entrada.texto_destino
        else:
            texto_pregunta = entrada.texto_destino
            respuesta_correcta = entrada.texto_origen

        preguntas.append(
            {
                "orden": orden,
                "entrada_id": entrada.id,
                "tema_id": entrada.tema_id,
                "sentido": sentido_pregunta,
                "texto_pregunta": texto_pregunta,
                "respuesta_correcta": respuesta_correcta,
            }
        )

    return preguntas


def normalizar_texto(valor):
    valor = (valor or "").strip().casefold()
    valor = unicodedata.normalize("NFKD", valor)
    return "".join(
        caracter
        for caracter in valor
        if not unicodedata.combining(caracter)
    )


def respuesta_es_correcta(respuesta_usuario, respuesta_correcta):
    return normalizar_texto(respuesta_usuario) == normalizar_texto(
        respuesta_correcta
    )


def calificacion_examen(nota):
    if nota >= 9:
        return "Sobresaliente"
    if nota >= 7:
        return "Notable"
    if nota >= 5:
        return "Aprobado"
    return "Necesita mejorar"
