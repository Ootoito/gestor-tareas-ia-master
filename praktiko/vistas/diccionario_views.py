from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Q
from django.shortcuts import get_object_or_404, redirect, render

from praktiko.forms.diccionario_forms import DiccionarioForm
from praktiko.models import Diccionario


@login_required
def listado_diccionarios(request):
    diccionarios = (
        Diccionario.objects
        .filter(
            Q(usuario=request.user)
            |
            Q(
                grupo__miembros__usuario=request.user,
            grupo__miembros__activo=True,
            grupo__activo=True,
        )
    )
    .distinct()
    .annotate(
        total_temas=Count("temas", distinct=True),
        total_entradas=Count("entradas", distinct=True),
    )
    .order_by("nombre")
)

    return render(
        request,
        "praktiko/diccionarios/listado.html",
        {
            "diccionarios": diccionarios,
        },
    )


@login_required
def crear_diccionario(request):
    if request.method == "POST":
        form = DiccionarioForm(request.POST)

        if form.is_valid():
            diccionario = form.save(commit=False)
            diccionario.usuario = request.user
            diccionario.save()

            messages.success(request, "Diccionario creado correctamente.")
            return redirect("praktiko:listado_diccionarios")
    else:
        form = DiccionarioForm(
            initial={
                "idioma_destino": "Español",
                "icono": "📚",
                "color": "#2563eb",
                "activo": True,
            }
        )

    return render(
        request,
        "praktiko/diccionarios/formulario.html",
        {
            "form": form,
            "titulo": "Nuevo diccionario",
            "boton": "Crear diccionario",
        },
    )

@login_required
def editar_diccionario(request, diccionario_id):
    diccionario = get_object_or_404(
        Diccionario,
        id=diccionario_id,
        usuario=request.user,
    )

    if request.method == "POST":
        form = DiccionarioForm(request.POST, instance=diccionario)

        if form.is_valid():
            form.save()
            messages.success(request, "Diccionario actualizado correctamente.")
            return redirect("praktiko:listado_diccionarios")
    else:
        form = DiccionarioForm(instance=diccionario)

    return render(
        request,
        "praktiko/diccionarios/formulario.html",
        {
            "form": form,
            "titulo": "Editar diccionario",
            "boton": "Guardar cambios",
        },
    )