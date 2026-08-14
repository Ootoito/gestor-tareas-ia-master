from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.translation import gettext as _

from praktiko.forms.aprender_forms import ConfiguracionAprenderForm
from praktiko.servicios.aprender_service import obtener_entradas_ficha


@login_required
def configurar_aprender(request):
    if request.method == "POST":
        form = ConfiguracionAprenderForm(
            request.POST,
            usuario=request.user,
        )

        if form.is_valid():
            diccionario = form.cleaned_data["diccionario"]
            temas = form.cleaned_data["temas"]
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
