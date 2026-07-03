import os
from openai import OpenAI

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


def generar_recomendacion_openai(
    prompt,
    total_preguntas=0,
    porcentaje_global=0,
    total_palabras_dificiles=0,
    tema_principal=None,
):
    api_key = os.environ.get("OPENAI_API_KEY")
    modelo = os.environ.get("OPENAI_MODEL", "gpt-5.2")

    if not api_key:
        return {
            "titulo": "Modo prueba IA",
            "mensaje": (
                "No hay clave OPENAI_API_KEY configurada. "
                "Se muestra una recomendación local."
            ),
            "accion_principal": "estadisticas",
            "texto_boton": "📊 Ver estadísticas",
            "prioridad": "media",
            "detalle": prompt,
            "prompt": prompt,
        }

    client = OpenAI(api_key=api_key)

    prompt_final = f"""
Devuelve una recomendación de estudio en formato JSON válido.

No añadas texto fuera del JSON.

El JSON debe tener exactamente estas claves:
- titulo
- mensaje
- accion_principal
- texto_boton
- prioridad
- detalle

Valores permitidos para accion_principal:
- jugar_dificiles
- jugar_normal
- estadisticas

Valores permitidos para prioridad:
- baja
- media
- alta

Datos del usuario:
{prompt}
"""

    try:
        response = client.responses.create(
            model=modelo,
            input=prompt_final,
        )

        texto = response.output_text

        return convertir_respuesta_ia_a_dict(
            texto=texto,
            prompt=prompt,
            total_preguntas=total_preguntas,
            porcentaje_global=porcentaje_global,
            total_palabras_dificiles=total_palabras_dificiles,
        )

    except Exception as e:
        return {
            "titulo": "Error IA",
            "mensaje": "No se pudo generar la recomendación con IA.",
            "accion_principal": "estadisticas",
            "texto_boton": "📊 Ver estadísticas",
            "prioridad": "media",
            "detalle": f"Error: {e}",
            "prompt": prompt,
        }
    
def convertir_respuesta_ia_a_dict(
    texto,
    prompt,
    total_preguntas=0,
    porcentaje_global=0,
    total_palabras_dificiles=0,
):
    import json

    try:
        datos = json.loads(texto)

        return {
            "titulo": datos.get("titulo", "Recomendación de estudio"),
            "mensaje": datos.get("mensaje", ""),
            "accion_principal": datos.get("accion_principal", "estadisticas"),
            "texto_boton": datos.get("texto_boton", "📊 Ver estadísticas"),
            "prioridad": datos.get("prioridad", "media"),
            "detalle": datos.get("detalle", ""),
            "prompt": prompt,
        }

    except Exception:
        return generar_recomendacion_local_estructurada(
            prompt=prompt,
            total_preguntas=total_preguntas,
            porcentaje_global=porcentaje_global,
            total_palabras_dificiles=total_palabras_dificiles,
        )

def generar_recomendacion_local_estructurada(
    prompt,
    total_preguntas=0,
    porcentaje_global=0,
    total_palabras_dificiles=0,
):
    if total_preguntas == 0:
        return {
            "titulo": "Empieza a generar datos",
            "mensaje": (
                "Todavía no hay suficientes estadísticas para darte una "
                "recomendación personalizada."
            ),
            "accion_principal": "jugar_normal",
            "texto_boton": "🎮 Empezar una partida",
            "prioridad": "media",
            "detalle": (
                "Juega algunas partidas o realiza prácticas para que Praktiko "
                "pueda analizar tus aciertos y fallos."
            ),
            "prompt": prompt,
        }

    if total_palabras_dificiles >= 3:
        return {
            "titulo": "Refuerza tus palabras difíciles",
            "mensaje": (
                "Se han detectado varias palabras con bajo porcentaje de acierto."
            ),
            "accion_principal": "jugar_dificiles",
            "texto_boton": "🎮 Jugar palabras difíciles",
            "prioridad": "alta",
            "detalle": (
                "Empieza con una partida de palabras difíciles antes de añadir "
                "nuevo vocabulario."
            ),
            "prompt": prompt,
        }

    if porcentaje_global < 70:
        return {
            "titulo": "Consolida antes de avanzar",
            "mensaje": "Tu porcentaje global de acierto todavía puede mejorar.",
            "accion_principal": "estadisticas",
            "texto_boton": "📊 Ver estadísticas",
            "prioridad": "media",
            "detalle": "Revisa tus estadísticas y practica los temas con más fallos.",
            "prompt": prompt,
        }

    return {
        "titulo": "Buen progreso",
        "mensaje": (
            "Tu rendimiento general es positivo. Puedes continuar practicando "
            "o añadir nuevo vocabulario."
        ),
        "accion_principal": "jugar_normal",
        "texto_boton": "🎮 Jugar una partida",
        "prioridad": "baja",
        "detalle": "Mantén la práctica regular y sigue ampliando tus diccionarios.",
        "prompt": prompt,
    }
    
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

Genera exactamente {cantidad} palabras o frases cortas para estudiar.

Tema:
{tema}

Idioma origen:
{idioma_origen}

Idioma destino:
{idioma_destino}

Nivel:
{nivel}

NO repitas ninguna de estas palabras ya existentes:

{", ".join(palabras_existentes)}

Devuelve EXCLUSIVAMENTE un JSON válido.

Formato exacto:

[
    {{
        "origen": "...",
        "destino": "...",
        "tipo": "Palabra",
        "ejemplo_origen": "...",
        "ejemplo_destino": "..."
    }}
]

Reglas:
- "origen" debe estar en {idioma_origen}.
- "destino" debe estar en {idioma_destino}.
- "ejemplo_origen" debe ser una frase breve en {idioma_origen}.
- "ejemplo_destino" debe ser la traducción natural de esa frase en {idioma_destino}.
- El campo "tipo" solo puede ser "Palabra" o "Frase".
- No incluyas palabras repetidas.
- No escribas explicaciones.
- No utilices markdown.
- No pongas ```json.
- Devuelve únicamente el JSON.
"""

    return prompt