from django.urls import path

from . import views
from . import views_gestion

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
    # URL GESTION DE LA PLATAFORMA (DCS)
    # ============================================================

    path(
        "gestion/login/",
        views_gestion.gestion_login,
        name="gestion_login",
    ),
    path(
        "gestion/logout/",
        views_gestion.gestion_logout,
        name="gestion_logout",
    ),
    path(
        "gestion/",
        views_gestion.gestion_panel,
        name="gestion",
    ),

    path(
        "gestion/aeronaves/<int:aeronave_id>/",
        views_gestion.gestion_aeronave,
        name="gestion_aeronave",
    ),

    path(
        "gestion/contenidos/<int:contenido_id>/misiones/",
        views_gestion.gestion_misiones,
        name="gestion_misiones",
    ),

    path(
        "gestion/misiones/<int:mision_id>/editar/",
        views_gestion.gestion_mision_editar,
        name="gestion_mision_editar",
    ),

    path(
        "gestion/contenidos/<int:contenido_id>/misiones/nueva/",
        views_gestion.gestion_mision_nueva,
        name="gestion_mision_nueva",
    ),

    path(
        "gestion/misiones/<int:mision_id>/eliminar/",
        views_gestion.gestion_mision_eliminar,
        name="gestion_mision_eliminar",
    ),

    # ============================================================
    # VERSIONES DE MISIÓN
    # ============================================================

    path(
        "gestion/misiones/<int:mision_id>/versiones/",
        views_gestion.gestion_versiones_mision,
        name="gestion_versiones_mision",
    ),

    path(
        "gestion/misiones/<int:mision_id>/versiones/nueva/",
        views_gestion.gestion_version_mision_nueva,
        name="gestion_version_mision_nueva",
    ),

    path(
        "gestion/versiones/<int:version_id>/editar/",
        views_gestion.gestion_version_mision_editar,
        name="gestion_version_mision_editar",
    ),

    path(
        "gestion/versiones/<int:version_id>/eliminar/",
        views_gestion.gestion_version_mision_eliminar,
        name="gestion_version_mision_eliminar",
    ),

    path(
        "gestion/aeronaves/<int:aeronave_id>/contenidos/nuevo/",
        views_gestion.gestion_contenido_nuevo,
        name="gestion_contenido_nuevo",
    ),

    path(
        "gestion/contenidos/<int:contenido_id>/editar/",
        views_gestion.gestion_contenido_editar,
        name="gestion_contenido_editar",
    ),

    path(
        "gestion/contenidos/<int:contenido_id>/eliminar/",
        views_gestion.gestion_contenido_eliminar,
        name="gestion_contenido_eliminar",
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
