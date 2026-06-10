from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render

from praktiko.forms.tema_forms import TemaForm
from praktiko.models import Tema


@login_required
def listado_temas(request):
    temas = (
        Tema.objects
        .filter(usuario=request.user)
        .select_related("diccionario")
        .annotate(total_entradas=Count("entradas", distinct=True))
        .order_by("diccionario__nombre", "orden", "nombre")
    )

    return render(
        request,
        "praktiko/temas/listado.html",
        {
            "temas": temas,
        },
    )


@login_required
def crear_tema(request):
    if request.method == "POST":
        form = TemaForm(request.POST, usuario=request.user)

        if form.is_valid():
            tema = form.save(commit=False)
            tema.usuario = request.user
            tema.save()

            messages.success(request, "Tema creado correctamente.")
            return redirect("praktiko:listado_temas")
    else:
        form = TemaForm(
            usuario=request.user,
            initial={
                "icono": "📁",
                "color": "#64748b",
                "orden": 0,
                "activo": True,
            },
        )

    return render(
        request,
        "praktiko/temas/formulario.html",
        {
            "form": form,
            "titulo": "Nuevo tema",
            "boton": "Crear tema",
        },
    )

@login_required
def editar_tema(request, tema_id):
    tema = get_object_or_404(
        Tema,
        id=tema_id,
        usuario=request.user,
    )

    if request.method == "POST":
        form = TemaForm(
            request.POST,
            instance=tema,
            usuario=request.user,
        )

        if form.is_valid():
            form.save()
            messages.success(request, "Tema actualizado correctamente.")
            return redirect("praktiko:listado_temas")
    else:
        form = TemaForm(
            instance=tema,
            usuario=request.user,
        )

    return render(
        request,
        "praktiko/temas/formulario.html",
        {
            "form": form,
            "titulo": "Editar tema",
            "boton": "Guardar cambios",
        },
    )

