import os
from openai import OpenAI


def generar_resumen_ia_gestor(datos_dashboard):
    api_key = os.environ.get("OPENAI_API_KEY")
    modelo = os.environ.get("OPENAI_MODEL", "gpt-5.2")

    if not api_key:
        return (
            "No hay clave de API configurada. "
            "Configura OPENAI_API_KEY en el archivo .env para activar el resumen IA."
        )

    client = OpenAI(api_key=api_key)

    prompt = f"""
Analiza estos datos de un gestor de tareas y genera un resumen breve, claro y útil.

Datos:
- Grupo: {datos_dashboard["grupo"]}
- Total tareas: {datos_dashboard["total_tareas"]}
- Pendientes: {datos_dashboard["total_pendientes"]}
- Pendientes de firma: {datos_dashboard["total_pendientes_firma"]}
- Pendientes de devolución: {datos_dashboard["total_pendientes_devolucion"]}
- Programadas: {datos_dashboard["total_programadas"]}
- Urgentes: {datos_dashboard["total_urgentes"]}
- Completadas: {datos_dashboard["total_completadas"]}

Tareas por técnico:
{datos_dashboard["tareas_por_tecnico"]}

Devuelve:
1. Diagnóstico general.
2. Riesgos detectados.
3. Recomendaciones concretas.
Máximo 8 líneas.
"""

    try:
        response = client.responses.create(
            model=modelo,
            input=prompt,
        )
        return response.output_text

    except Exception as e:
        return f"No se pudo generar el resumen IA: {e}"