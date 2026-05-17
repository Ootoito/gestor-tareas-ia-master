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
    
def generar_subtareas_ia(tarea):
    api_key = os.environ.get("OPENAI_API_KEY")
    modelo = os.environ.get("OPENAI_MODEL", "gpt-5.2")

    if not api_key:
        return "No hay clave OPENAI_API_KEY configurada."

    client = OpenAI(api_key=api_key)

    prompt = f"""
Analiza esta tarea y genera una lista breve de subtareas accionables.

Título: {tarea.titulo}
Descripción: {tarea.descripcion or ""}
Estado: {tarea.estado.nombre if tarea.estado else ""}
Prioridad: {tarea.prioridad}
Ámbito: {tarea.ambito.nombre if tarea.ambito else ""}
Técnico asignado: {tarea.tecnico.nombre if tarea.tecnico else "Sin asignar"}

Devuelve únicamente una lista numerada de entre 4 y 7 subtareas concretas.
No añadas introducción ni conclusión.
"""

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
    
def analizar_prioridad_ia(tarea):

    api_key = os.environ.get("OPENAI_API_KEY")
    modelo = os.environ.get("OPENAI_MODEL", "gpt-5.2")

    if not api_key:
        return "No hay clave OPENAI_API_KEY configurada."

    client = OpenAI(api_key=api_key)

    prompt = f"""
Analiza esta tarea y recomienda una prioridad.

Título:
{tarea.titulo}

Descripción:
{tarea.descripcion or ""}

Fecha objetivo:
{tarea.fecha_objetivo}

Estado:
{tarea.estado.nombre if tarea.estado else ""}

Devuelve EXACTAMENTE:

PRIORIDAD: <Baja|Normal|Alta|Urgente>

MOTIVO:
<explicación breve>
"""

    try:

        response = client.responses.create(
            model=modelo,
            input=prompt,
        )

        return response.output_text

    except Exception as e:

        texto_error = str(e)

        if "insufficient_quota" in texto_error:
            return "La IA está integrada, pero la cuenta API no tiene saldo."

        return f"Error IA: {e}"