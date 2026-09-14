from django.urls import path

from . import views


app_name = "dcs"


urlpatterns = [
    # ============================================================
    # PÁGINAS GENERALES
    # ============================================================

    path(
        "",
        views.inicio,
        name="inicio",
    ),

    path(
        "misiones/",
        views.misiones,
        name="misiones",
    ),

    # ============================================================
    # COMPATIBILIDAD CON LAS URL ANTIGUAS DEL F-4E
    # ============================================================

    path(
        "f4e/",
        views.f4e_legacy,
        name="f4e",
    ),

    path(
        "f4e/curso/",
        views.f4e_curso_legacy,
        name="f4e_curso",
    ),

    path(
        "f4e/fuego-en-el-estrecho/",
        views.f4e_fuego_legacy,
        name="f4e_fuego_estrecho",
    ),

    path(
        "f4e/phantoms-over-marianas/",
        views.f4e_marianas_legacy,
        name="f4e_marianas",
    ),

    # ============================================================
    # URL GENÉRICA DE AERONAVE
    # ============================================================

    path(
        "<slug:aeronave_slug>/",
        views.aeronave_detalle,
        name="aeronave",
    ),

    # ============================================================
    # URL GENÉRICA DE CURSO / CAMPAÑA / COLECCIÓN
    # ============================================================

    path(
        "<slug:aeronave_slug>/<slug:contenido_slug>/",
        views.contenido_detalle,
        name="contenido",
    ),
]