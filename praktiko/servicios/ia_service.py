def generar_prompt_recomendacion(
    porcentaje_global,
    total_preguntas,
    total_aciertos,
    total_fallos,
    palabras_dificiles,
    temas_problematicos,
    diccionario_principal,
    total_entradas_usuario,
    palabras_dominadas,
    porcentaje_7_dias,
    total_respuestas_7_dias,
    porcentaje_30_dias,
    total_respuestas_30_dias,
    tendencia,
):
    lineas = []

    lineas.append("Eres un asistente de aprendizaje de idiomas.")
    lineas.append("Analiza estos datos de progreso del usuario y genera una recomendación breve.")
    lineas.append("")
    lineas.append("Resumen global:")
    lineas.append(f"- Preguntas totales: {total_preguntas}")
    lineas.append(f"- Aciertos: {total_aciertos}")
    lineas.append(f"- Fallos: {total_fallos}")
    lineas.append(f"- Porcentaje global de acierto: {porcentaje_global}%")
    lineas.append("")

    lineas.append("Evolución temporal:")
    lineas.append(
        f"- Últimos 7 días: {porcentaje_7_dias}% "
        f"({total_respuestas_7_dias} respuestas)"
    )
    lineas.append(
        f"- Últimos 30 días: {porcentaje_30_dias}% "
        f"({total_respuestas_30_dias} respuestas)"
    )
    lineas.append(f"- Tendencia: {tendencia}")
    lineas.append("")

    lineas.append("Palabras difíciles:")

    if palabras_dificiles:
        for estadistica in palabras_dificiles[:10]:
            entrada = estadistica.entrada
            lineas.append(
                f"- {entrada.texto_origen} → {entrada.texto_destino} "
                f"({estadistica.fallos} fallos, {estadistica.porcentaje_acierto}% acierto)"
            )
    else:
        lineas.append("- No hay palabras difíciles suficientes.")

    lineas.append("")
    lineas.append("Temas problemáticos:")

    if temas_problematicos:
        for tema, fallos in temas_problematicos[:5]:
            lineas.append(f"- {tema}: {fallos} fallos")
    else:
        lineas.append("- No hay temas problemáticos detectados.")

    lineas.append("")
    lineas.append(f"Diccionario principal: {diccionario_principal}")
    lineas.append(f"Entradas totales del usuario: {total_entradas_usuario}")
    lineas.append(f"Palabras dominadas: {len(palabras_dominadas)}")
    lineas.append(f"Número de palabras difíciles: {len(palabras_dificiles)}")

    porcentaje_palabras_dominadas = (
        round((len(palabras_dominadas) / total_entradas_usuario) * 100, 2)
        if total_entradas_usuario
        else 0
    )

    lineas.append(
        f"Porcentaje de palabras dominadas: {porcentaje_palabras_dominadas}%"
    )

    lineas.append("")
    lineas.append("Ejemplos de palabras dominadas:")

    if palabras_dominadas:
        for estadistica in palabras_dominadas[:5]:
            entrada = estadistica.entrada
            lineas.append(
                f"- {entrada.texto_origen} → {entrada.texto_destino}"
            )
    else:
        lineas.append("- No hay suficientes palabras dominadas.")

    lineas.append("")

    if porcentaje_global >= 85:
        lineas.append("Nivel actual: avanzado en este diccionario.")
    elif porcentaje_global >= 70:
        lineas.append("Nivel actual: intermedio con buena progresión.")
    elif porcentaje_global >= 50:
        lineas.append("Nivel actual: en consolidación.")
    else:
        lineas.append("Nivel actual: requiere refuerzo de vocabulario básico.")

    lineas.append("")

    lineas.append(
        "Ten en cuenta la evolución temporal para distinguir si el usuario "
        "está mejorando, empeorando o manteniéndose estable."
    )

    lineas.append(
        "Indica además un objetivo razonable para la próxima semana "
        "basándote en el rendimiento global y en la tendencia reciente."
    )

    lineas.append("")

    lineas.append(
        "Genera una recomendación en español, clara y útil. "
        "Debe incluir qué repasar primero, qué tipo de práctica hacer, "
        "si conviene añadir nuevo vocabulario o consolidar el existente, "
        "y una valoración breve de la tendencia reciente."
    )

    return "\n".join(lineas)


def generar_recomendacion_openai(prompt):
    import os
    from openai import OpenAI

    api_key = os.environ.get("OPENAI_API_KEY")
    modelo = os.environ.get("OPENAI_MODEL", "gpt-5.2")

    if not api_key:
        return (
            "MODO PRUEBA IA\n\n"
            "No hay clave OPENAI_API_KEY configurada en el archivo .env.\n\n"
            "Este es el resumen que se enviaría al modelo:\n\n"
            f"{prompt}"
        )

    client = OpenAI(api_key=api_key)

    try:
        response = client.responses.create(
            model=modelo,
            input=prompt,
        )

        return response.output_text

    except Exception as e:
        texto_error = str(e)

        if "insufficient_quota" in texto_error:
            return "La IA está integrada, pero la cuenta API no tiene saldo disponible."

        return f"Error IA: {e}"
    
def generar_vocabulario_openai(prompt):
    import json
    import os

    from openai import OpenAI

    api_key = os.environ.get("OPENAI_API_KEY")
    modelo = os.environ.get("OPENAI_MODEL", "gpt-5.2")

    if not api_key:
        return {
            "ok": False,
            "error": "No existe OPENAI_API_KEY configurada."
        }

    client = OpenAI(api_key=api_key)

    try:

        response = client.responses.create(
            model=modelo,
            input=prompt,
        )

        texto = response.output_text.strip()

        return {
            "ok": True,
            "datos": json.loads(texto),
        }

    except Exception as e:

        return {
            "ok": False,
            "error": str(e),
        }

def generar_prompt_vocabulario(
    idioma_origen,
    idioma_destino,
    tema,
    nivel,
    cantidad,
    palabras_existentes,
):
    prompt = f"""
Eres un profesor de idiomas.

Genera exactamente {cantidad} palabras o frases cortas.

Tema:
{tema}

Idioma origen:
{idioma_origen}

Idioma destino:
{idioma_destino}

Nivel:
{nivel}

NO repitas ninguna de estas palabras:

{", ".join(palabras_existentes)}

Devuelve EXCLUSIVAMENTE un JSON válido.

Formato:

[
    {{
        "origen":"...",
        "destino":"...",
        "tipo":"Palabra"
    }}
]

No escribas explicaciones.
No utilices markdown.
No pongas json.
Devuelve únicamente el JSON.
"""

    return prompt