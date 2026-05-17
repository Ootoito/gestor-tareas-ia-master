import os
from openai import OpenAI


def generar_resumen_ia_gestor(datos_dashboard):

    api_key = os.environ.get("OPENAI_API_KEY")
    modelo = os.environ.get("OPENAI_MODEL", "gpt-5.2")

    if not api_key:
        return (
            "No hay clave OPENAI_API_KEY configurada "
            "en el archivo .env"
        )

    client = OpenAI(api_key=api_key)

    prompt = f"""
Analiza estos datos de un gestor de tareas.

Grupo: {datos_dashboard["grupo"]}

Total tareas: {datos_dashboard["total_tareas"]}
Pendientes: {datos_dashboard["total_pendientes"]}
Pendientes firma: {datos_dashboard["total_pendientes_firma"]}
Pendientes devolución: {datos_dashboard["total_pendientes_devolucion"]}
Programadas: {datos_dashboard["total_programadas"]}
Urgentes: {datos_dashboard["total_urgentes"]}
Completadas: {datos_dashboard["total_completadas"]}

Tareas por técnico:
{datos_dashboard["tareas_por_tecnico"]}

Genera:
- diagnóstico general
- riesgos
- recomendaciones

Máximo 8 líneas.
"""

    try:

        response = client.responses.create(
            model=modelo,
            input=prompt,
        )

        return response.output_text

    except Exception as e:
        return f"Error IA: {e}"