import random

from praktiko.models import EntradaDiccionario


def obtener_entradas_ficha(
    *,
    usuario,
    diccionario,
    temas=None,
    cantidad=15,
    modo_seleccion="aleatorio",
):
    """
    Devuelve las entradas que formarán una ficha de estudio.

    La primera versión trabaja únicamente con vocabulario personal del usuario.
    No modifica estadísticas ni persiste una sesión de aprendizaje.
    """

    entradas = EntradaDiccionario.objects.filter(
        usuario=usuario,
        diccionario=diccionario,
        activa=True,
    ).select_related(
        "diccionario",
        "tema",
    )

    if temas:
        temas_ids = [tema.id for tema in temas]
        if temas_ids:
            entradas = entradas.filter(tema_id__in=temas_ids)

    total_disponibles = entradas.count()

    if total_disponibles < cantidad:
        return [], total_disponibles

    if modo_seleccion == "orden":
        seleccionadas = list(
            entradas.order_by(
                "tema__orden",
                "tema__nombre",
                "texto_origen",
            )[:cantidad]
        )
    else:
        ids = list(entradas.values_list("id", flat=True))
        ids_seleccionados = random.sample(ids, cantidad)

        entradas_por_id = {
            entrada.id: entrada
            for entrada in entradas.filter(id__in=ids_seleccionados)
        }

        # Conserva el orden aleatorio producido por random.sample().
        seleccionadas = [
            entradas_por_id[entrada_id]
            for entrada_id in ids_seleccionados
        ]

    return seleccionadas, total_disponibles
