from django.shortcuts import get_object_or_404, redirect, render

from .models import Aeronave, ContenidoDCS


def inicio(request):
    return render(
        request,
        "dcs/index.html",
    )


def misiones(request):
    aeronaves = (
        Aeronave.objects
        .filter(activo=True)
        .order_by(
            "orden",
            "nombre",
        )
    )

    return render(
        request,
        "dcs/misiones.html",
        {
            "aeronaves": aeronaves,
        },
    )


# ============================================================
# VISTA GENÉRICA DE AERONAVE
# ============================================================

def aeronave_detalle(request, aeronave_slug):
    aeronave = get_object_or_404(
        Aeronave,
        slug=aeronave_slug,
        activo=True,
    )

    contenidos = (
        aeronave.contenidos
        .filter(activo=True)
        .exclude(
            estado=ContenidoDCS.ESTADO_OCULTO,
        )
        .order_by(
            "orden",
            "titulo",
        )
    )

    return render(
        request,
        "dcs/aeronave.html",
        {
            "aeronave": aeronave,
            "contenidos": contenidos,
        },
    )


# ============================================================
# VISTA GENÉRICA DE CONTENIDO
# ============================================================

def contenido_detalle(
    request,
    aeronave_slug,
    contenido_slug,
):
    contenido = get_object_or_404(
        ContenidoDCS.objects.select_related(
            "aeronave",
        ),
        aeronave__slug=aeronave_slug,
        aeronave__activo=True,
        slug=contenido_slug,
        activo=True,
    )

    if contenido.estado == ContenidoDCS.ESTADO_OCULTO:
        return redirect(
            "dcs:aeronave",
            aeronave_slug=contenido.aeronave.slug,
        )

    misiones = (
        contenido.misiones
        .filter(activo=True)
        .order_by(
            "orden",
            "numero",
        )
    )

    return render(
        request,
        "dcs/contenido.html",
        {
            "aeronave": contenido.aeronave,
            "contenido": contenido,
            "misiones": misiones,
        },
    )


# ============================================================
# URL ANTIGUAS DEL F-4E
#
# Las mantenemos para no romper enlaces existentes.
# Todas redirigen ahora a las nuevas páginas genéricas.
# ============================================================

def f4e_legacy(request):
    return redirect(
        "dcs:aeronave",
        aeronave_slug="f4e-phantom-ii",
    )


def f4e_curso_legacy(request):
    return redirect(
        "dcs:contenido",
        aeronave_slug="f4e-phantom-ii",
        contenido_slug="phantom-flight-school",
    )


def f4e_fuego_legacy(request):
    return redirect(
        "dcs:contenido",
        aeronave_slug="f4e-phantom-ii",
        contenido_slug="fuego-en-el-estrecho",
    )


def f4e_marianas_legacy(request):
    return redirect(
        "dcs:contenido",
        aeronave_slug="f4e-phantom-ii",
        contenido_slug="phantoms-over-marianas",
    )