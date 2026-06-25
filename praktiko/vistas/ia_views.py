from collections import Counter
from datetime import timedelta

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils import timezone

from praktiko.models import (
    Diccionario,
    EstadisticaEntradaUsuario,
    EntradaDiccionario,
    RespuestaPractica,
    Tema,
)

from praktiko.servicios.ia_service import (
    generar_prompt_recomendacion,
    generar_recomendacion_openai,
    generar_prompt_vocabulario,
    generar_vocabulario_openai,
)


def obtener_criterios_dominio(total_preguntas):
    if total_preguntas < 50:
        return 3, 75
    elif total_preguntas < 150:
        return 4, 80
    elif total_preguntas < 500:
        return 5, 85
    else:
        return 7, 90


def calcular_porcentaje_respuestas(respuestas):
    total = respuestas.count()

    if total == 0:
        return 0, 0

    aciertos = respuestas.filter(correcta=True).count()
    porcentaje = round((aciertos / total) * 100, 2)

    return porcentaje, total


def calcular_tendencia(porcentaje_7_dias, porcentaje_30_dias):
    if porcentaje_7_dias == 0 and porcentaje_30_dias == 0:
        return "Sin datos suficientes"

    if porcentaje_7_dias > porcentaje_30_dias + 5:
        return "Mejorando"

    if porcentaje_7_dias < porcentaje_30_dias - 5:
        return "Empeorando"

    return "Estable"


def normalizar_tipo_entrada(tipo):
    tipo_normalizado = (tipo or "").strip().lower()

    if "frase" in tipo_normalizado:
        return EntradaDiccionario.TIPO_FRASE

    return EntradaDiccionario.TIPO_PALABRA


@login_required
def asistente_ia(request):
    return render(
        request,
        "praktiko/ia/asistente.html",
    )


@login_required
def recomendacion_estudio(request):
    estadisticas = (
        EstadisticaEntradaUsuario.objects
        .filter(
            usuario=request.user,
            veces_preguntada__gte=1,
        )
        .select_related(
            "entrada",
            "entrada__diccionario",
            "entrada__tema",
        )
    )

    total_preguntas = sum(e.veces_preguntada for e in estadisticas)
    total_aciertos = sum(e.aciertos for e in estadisticas)
    total_fallos = sum(e.fallos for e in estadisticas)

    porcentaje_global = 0

    if total_preguntas > 0:
        porcentaje_global = round(
            (total_aciertos / total_preguntas) * 100,
            2,
        )

    ahora = timezone.now()
    fecha_7_dias = ahora - timedelta(days=7)
    fecha_30_dias = ahora - timedelta(days=30)

    respuestas_7_dias = RespuestaPractica.objects.filter(
        sesion__usuario=request.user,
        respondida_en__gte=fecha_7_dias,
    )

    respuestas_30_dias = RespuestaPractica.objects.filter(
        sesion__usuario=request.user,
        respondida_en__gte=fecha_30_dias,
    )

    porcentaje_7_dias, total_respuestas_7_dias = calcular_porcentaje_respuestas(
        respuestas_7_dias
    )

    porcentaje_30_dias, total_respuestas_30_dias = calcular_porcentaje_respuestas(
        respuestas_30_dias
    )

    tendencia = calcular_tendencia(
        porcentaje_7_dias,
        porcentaje_30_dias,
    )

    minimo_preguntas_dominio, minimo_porcentaje_dominio = (
        obtener_criterios_dominio(total_preguntas)
    )

    diccionario_principal = None
    contador_diccionarios_uso = Counter()

    for e in estadisticas:
        contador_diccionarios_uso[
            e.entrada.diccionario.nombre
        ] += e.veces_preguntada

    if contador_diccionarios_uso:
        diccionario_principal = (
            contador_diccionarios_uso
            .most_common(1)[0][0]
        )

    palabras_dominadas = [
        e
        for e in estadisticas
        if (
            e.veces_preguntada >= minimo_preguntas_dominio
            and e.porcentaje_acierto >= minimo_porcentaje_dominio
        )
    ]

    palabras_dificiles = [
        e
        for e in estadisticas
        if e.veces_preguntada >= 3 and e.porcentaje_acierto < 60
    ]

    palabras_dificiles = sorted(
        palabras_dificiles,
        key=lambda e: (e.fallos, e.veces_preguntada),
        reverse=True,
    )[:10]

    total_entradas_usuario = EntradaDiccionario.objects.filter(
        usuario=request.user,
        activa=True,
    ).count()

    contador_temas = Counter()
    contador_diccionarios = Counter()

    for e in estadisticas:
        if e.fallos > 0:
            if e.entrada.tema:
                contador_temas[e.entrada.tema.nombre] += e.fallos

            contador_diccionarios[e.entrada.diccionario.nombre] += e.fallos

    temas_problematicos = contador_temas.most_common(5)
    diccionarios_problematicos = contador_diccionarios.most_common(5)

    recomendaciones = []

    if palabras_dificiles:
        recomendaciones.append(
            "Empieza con una partida de palabras difíciles."
        )

    if temas_problematicos:
        recomendaciones.append(
            f"Repasa especialmente el tema «{temas_problematicos[0][0]}»."
        )

    if porcentaje_global < 70 and total_preguntas > 0:
        recomendaciones.append(
            "Haz una práctica corta antes de jugar para reforzar memoria."
        )

    if tendencia == "Empeorando":
        recomendaciones.append(
            "Tu tendencia reciente ha bajado. Conviene hacer repasos cortos antes de añadir vocabulario nuevo."
        )

    if tendencia == "Mejorando":
        recomendaciones.append(
            "Tu tendencia reciente mejora. Puedes mantener el ritmo actual y añadir vocabulario con prudencia."
        )

    if not recomendaciones:
        recomendaciones.append(
            "Tu progreso es bueno. Continúa practicando con partidas normales."
        )

    prompt_ia = generar_prompt_recomendacion(
        porcentaje_global=porcentaje_global,
        total_preguntas=total_preguntas,
        total_aciertos=total_aciertos,
        total_fallos=total_fallos,
        palabras_dificiles=palabras_dificiles,
        temas_problematicos=temas_problematicos,
        diccionario_principal=diccionario_principal,
        total_entradas_usuario=total_entradas_usuario,
        palabras_dominadas=palabras_dominadas,
        porcentaje_7_dias=porcentaje_7_dias,
        total_respuestas_7_dias=total_respuestas_7_dias,
        porcentaje_30_dias=porcentaje_30_dias,
        total_respuestas_30_dias=total_respuestas_30_dias,
        tendencia=tendencia,
    )

    informe_ia = generar_recomendacion_openai(prompt_ia)

    return render(
        request,
        "praktiko/ia/recomendacion_estudio.html",
        {
            "palabras_dificiles": palabras_dificiles,
            "temas_problematicos": temas_problematicos,
            "diccionarios_problematicos": diccionarios_problematicos,
            "total_preguntas": total_preguntas,
            "total_aciertos": total_aciertos,
            "total_fallos": total_fallos,
            "porcentaje_global": porcentaje_global,
            "recomendaciones": recomendaciones,
            "informe_ia": informe_ia,
            "prompt_ia": prompt_ia,
            "minimo_preguntas_dominio": minimo_preguntas_dominio,
            "minimo_porcentaje_dominio": minimo_porcentaje_dominio,
            "porcentaje_7_dias": porcentaje_7_dias,
            "total_respuestas_7_dias": total_respuestas_7_dias,
            "porcentaje_30_dias": porcentaje_30_dias,
            "total_respuestas_30_dias": total_respuestas_30_dias,
            "tendencia": tendencia,
        },
    )


@login_required
def crear_vocabulario_tema(request):
    diccionarios = (
        Diccionario.objects
        .filter(
            usuario=request.user,
            activo=True,
        )
        .order_by("nombre")
    )

    for diccionario in diccionarios:
        diccionario.total_entradas_activas = (
            EntradaDiccionario.objects
            .filter(
                usuario=request.user,
                diccionario=diccionario,
                activa=True,
            )
            .count()
        )

    resultado = None
    resumen_guardado = None

    if request.method == "POST":
        accion = request.POST.get("accion", "generar")
        diccionario_id = request.POST.get("diccionario")
        tema_nombre = request.POST.get("tema", "").strip()
        cantidad = request.POST.get("cantidad")
        nivel = request.POST.get("nivel")

        diccionario = (
            Diccionario.objects
            .filter(
                id=diccionario_id,
                usuario=request.user,
                activo=True,
            )
            .first()
        )

        if diccionario and accion == "guardar":
            tema, _ = Tema.objects.get_or_create(
                usuario=request.user,
                diccionario=diccionario,
                nombre=tema_nombre,
                defaults={
                    "icono": "📁",
                    "color": "#64748b",
                    "activo": True,
                },
            )

            indices_seleccionados = request.POST.getlist("seleccionadas")

            creadas = 0
            duplicadas = 0
            errores = 0

            for indice in indices_seleccionados:
                origen = request.POST.get(f"origen_{indice}", "").strip()
                destino = request.POST.get(f"destino_{indice}", "").strip()
                tipo = request.POST.get(f"tipo_{indice}", "").strip()

                if not origen or not destino:
                    errores += 1
                    continue

                ya_existe = EntradaDiccionario.objects.filter(
                    usuario=request.user,
                    diccionario=diccionario,
                    texto_origen__iexact=origen,
                ).exists()

                if ya_existe:
                    duplicadas += 1
                    continue

                EntradaDiccionario.objects.create(
                    usuario=request.user,
                    diccionario=diccionario,
                    tema=tema,
                    tipo=normalizar_tipo_entrada(tipo),
                    texto_origen=origen,
                    texto_destino=destino,
                    nivel=nivel,
                    activa=True,
                )

                creadas += 1

            resumen_guardado = {
                "diccionario": diccionario,
                "tema": tema,
                "seleccionadas": len(indices_seleccionados),
                "creadas": creadas,
                "duplicadas": duplicadas,
                "errores": errores,
            }

        elif diccionario and accion == "generar":
            palabras_existentes = list(
                EntradaDiccionario.objects
                .filter(
                    usuario=request.user,
                    diccionario=diccionario,
                    activa=True,
                )
                .values_list(
                    "texto_origen",
                    flat=True,
                )
                .order_by("texto_origen")
            )

            tema_existente = None

            if tema_nombre:
                tema_existente = (
                    Tema.objects
                    .filter(
                        usuario=request.user,
                        diccionario=diccionario,
                        nombre__iexact=tema_nombre,
                    )
                    .first()
                )

            prompt = generar_prompt_vocabulario(
                idioma_origen=diccionario.idioma_origen,
                idioma_destino=diccionario.idioma_destino,
                tema=tema_nombre,
                nivel=nivel,
                cantidad=cantidad,
                palabras_existentes=palabras_existentes,
            )

            respuesta = generar_vocabulario_openai(prompt)

            resultado = {
                "diccionario": diccionario,
                "tema": tema_nombre,
                "tema_existe": tema_existente is not None,
                "nivel": nivel,
                "cantidad": cantidad,
                "total_palabras_existentes": len(palabras_existentes),
                "palabras_existentes_muestra": palabras_existentes[:25],
                "prompt": prompt,
                "respuesta": respuesta,
            }

    return render(
        request,
        "praktiko/ia/crear_vocabulario.html",
        {
            "diccionarios": diccionarios,
            "resultado": resultado,
            "resumen_guardado": resumen_guardado,
        },
    )