from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.translation import gettext as _

from praktiko.forms.aprender_forms import ConfiguracionAprenderForm
from praktiko.models import Diccionario, EntradaDiccionario, Tema
from praktiko.servicios.aprender_service import obtener_entradas_ficha


CLAVE_FICHA_APRENDER = "praktiko_ficha_aprender"


def _guardar_ficha_en_sesion(
    request,
    *,
    diccionario,
    temas,
    entradas,
    cantidad,
    incluir_ejemplos,
):
    """Guarda únicamente los datos necesarios para reproducir la misma ficha."""
    request.session[CLAVE_FICHA_APRENDER] = {
        "diccionario_id": diccionario.id,
        "temas_ids": [tema.id for tema in temas],
        "entradas_ids": [entrada.id for entrada in entradas],
        "cantidad": cantidad,
        "incluir_ejemplos": incluir_ejemplos,
    }


def _recuperar_ficha_de_sesion(request):
    """Recupera la ficha manteniendo exactamente el orden de sus entradas."""
    datos = request.session.get(CLAVE_FICHA_APRENDER)

    if not datos:
        return None

    diccionario = get_object_or_404(
        Diccionario,
        id=datos.get("diccionario_id"),
        usuario=request.user,
        activo=True,
        grupo__isnull=True,
    )

    temas_ids = datos.get("temas_ids", [])
    temas = list(
        Tema.objects.filter(
            id__in=temas_ids,
            usuario=request.user,
            diccionario=diccionario,
            activo=True,
        ).order_by("orden", "nombre")
    )

    entradas_ids = datos.get("entradas_ids", [])
    entradas_qs = (
        EntradaDiccionario.objects
        .filter(
            id__in=entradas_ids,
            usuario=request.user,
            diccionario=diccionario,
            activa=True,
        )
        .select_related("tema", "diccionario")
    )

    entradas_por_id = {
        entrada.id: entrada
        for entrada in entradas_qs
    }

    entradas = [
        entradas_por_id[entrada_id]
        for entrada_id in entradas_ids
        if entrada_id in entradas_por_id
    ]

    if not entradas:
        return None

    return {
        "diccionario": diccionario,
        "temas": temas,
        "entradas": entradas,
        "cantidad": len(entradas),
        "incluir_ejemplos": bool(datos.get("incluir_ejemplos", False)),
    }


@login_required
def configurar_aprender(request):
    if request.method == "POST":
        form = ConfiguracionAprenderForm(
            request.POST,
            usuario=request.user,
        )

        if form.is_valid():
            diccionario = form.cleaned_data["diccionario"]
            temas = list(form.cleaned_data["temas"])
            modo_seleccion = form.cleaned_data["modo_seleccion"]
            cantidad = form.cleaned_data["cantidad"]
            incluir_ejemplos = form.cleaned_data["incluir_ejemplos"]

            entradas, total_disponibles = obtener_entradas_ficha(
                usuario=request.user,
                diccionario=diccionario,
                temas=temas,
                cantidad=cantidad,
                modo_seleccion=modo_seleccion,
            )

            if not entradas:
                messages.error(
                    request,
                    _(
                        "No hay vocabulario suficiente para crear una ficha "
                        "de %(cantidad)s elementos. Hay %(disponibles)s "
                        "entradas disponibles con los filtros seleccionados."
                    )
                    % {
                        "cantidad": cantidad,
                        "disponibles": total_disponibles,
                    },
                )
            else:
                _guardar_ficha_en_sesion(
                    request,
                    diccionario=diccionario,
                    temas=temas,
                    entradas=entradas,
                    cantidad=cantidad,
                    incluir_ejemplos=incluir_ejemplos,
                )

                return render(
                    request,
                    "praktiko/aprender/ficha.html",
                    {
                        "diccionario": diccionario,
                        "temas": temas,
                        "entradas": entradas,
                        "cantidad": cantidad,
                        "modo_seleccion": modo_seleccion,
                        "incluir_ejemplos": incluir_ejemplos,
                    },
                )
    else:
        form = ConfiguracionAprenderForm(usuario=request.user)

    return render(
        request,
        "praktiko/aprender/configurar.html",
        {
            "form": form,
        },
    )


@login_required
def imprimir_ficha_aprender(request):
    ficha = _recuperar_ficha_de_sesion(request)

    if not ficha:
        messages.error(
            request,
            _(
                "No hay ninguna ficha de estudio preparada. "
                "Crea una ficha antes de abrir la versión para imprimir."
            ),
        )
        return redirect("praktiko:aprender_configurar")

    return render(
        request,
        "praktiko/aprender/ficha_imprimir.html",
        ficha,
    )
