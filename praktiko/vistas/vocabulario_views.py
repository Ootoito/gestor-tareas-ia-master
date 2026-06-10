from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from praktiko.forms.vocabulario_forms import EntradaDiccionarioForm
from praktiko.models import EntradaDiccionario


@login_required
def listado_vocabulario(request):
    entradas = (
        EntradaDiccionario.objects
        .filter(usuario=request.user)
        .select_related("diccionario", "tema")
        .order_by("diccionario__nombre", "tema__orden", "tema__nombre", "texto_origen")
    )

    return render(
        request,
        "praktiko/vocabulario/listado.html",
        {"entradas": entradas},
    )


@login_required
def crear_entrada(request):
    if request.method == "POST":
        form = EntradaDiccionarioForm(request.POST, usuario=request.user)

        if form.is_valid():
            entrada = form.save(commit=False)
            entrada.usuario = request.user
            entrada.save()

            messages.success(request, "Entrada creada correctamente.")
            return redirect("praktiko:listado_vocabulario")
    else:
        form = EntradaDiccionarioForm(
            usuario=request.user,
            initial={
                "tipo": EntradaDiccionario.TIPO_PALABRA,
                "nivel": EntradaDiccionario.NIVEL_INICIAL,
                "activa": True,
            },
        )

    return render(
        request,
        "praktiko/vocabulario/formulario.html",
        {
            "form": form,
            "titulo": "Nueva entrada",
            "boton": "Crear entrada",
        },
    )


@login_required
def editar_entrada(request, entrada_id):
    entrada = get_object_or_404(
        EntradaDiccionario,
        id=entrada_id,
        usuario=request.user,
    )

    if request.method == "POST":
        form = EntradaDiccionarioForm(
            request.POST,
            instance=entrada,
            usuario=request.user,
        )

        if form.is_valid():
            form.save()
            messages.success(request, "Entrada actualizada correctamente.")
            return redirect("praktiko:listado_vocabulario")
    else:
        form = EntradaDiccionarioForm(
            instance=entrada,
            usuario=request.user,
        )

    return render(
        request,
        "praktiko/vocabulario/formulario.html",
        {
            "form": form,
            "titulo": "Editar entrada",
            "boton": "Guardar cambios",
        },
    )