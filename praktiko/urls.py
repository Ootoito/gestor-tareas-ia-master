from django.urls import path

from praktiko.vistas import auth_views
from praktiko.vistas import home_views
from praktiko.vistas import diccionario_views
from praktiko.vistas import tema_views
from praktiko.vistas import vocabulario_views
from praktiko.vistas import practica_views
from praktiko.vistas import gestion_views
from praktiko.vistas import juego_views
from praktiko.vistas import importacion_views
from praktiko.vistas import grupo_views
from praktiko.vistas import estadistica_views

app_name = "praktiko"

urlpatterns = [
    path("login/", auth_views.login_praktiko, name="login"),
    path("logout/", auth_views.logout_praktiko, name="logout"),

    path("gestion/usuarios/", gestion_views.listado_usuarios, name="gestion_usuarios"),
    path("gestion/usuarios/<int:usuario_id>/estado/", gestion_views.cambiar_estado_usuario, name="gestion_cambiar_estado_usuario",),
    path("gestion/usuarios/<int:usuario_id>/reset-password/", gestion_views.resetear_password_usuario, name="gestion_resetear_password_usuario",),
    path("gestion/usuarios/nuevo/", gestion_views.crear_usuario, name="gestion_crear_usuario",),
    path("gestion/usuarios/<int:usuario_id>/editar/", gestion_views.editar_usuario, name="gestion_editar_usuario",),

    path("", home_views.home, name="home"),
    
    path("diccionarios/", diccionario_views.listado_diccionarios, name="listado_diccionarios"),
    path("diccionarios/nuevo/", diccionario_views.crear_diccionario, name="crear_diccionario"),
    path("diccionarios/<int:diccionario_id>/editar/", diccionario_views.editar_diccionario, name="editar_diccionario"),

    path("temas/", tema_views.listado_temas, name="listado_temas"),
    path("temas/nuevo/", tema_views.crear_tema, name="crear_tema"),
    path("temas/<int:tema_id>/editar/", tema_views.editar_tema, name="editar_tema"),

    path("vocabulario/", vocabulario_views.listado_vocabulario, name="listado_vocabulario"),
    path("vocabulario/nuevo/", vocabulario_views.crear_entrada, name="crear_entrada"),
    path("vocabulario/<int:entrada_id>/editar/", vocabulario_views.editar_entrada, name="editar_entrada"),

    path("practicar/", practica_views.configurar_practica, name="configurar_practica"),
    path("practicar/pregunta/", practica_views.pregunta_practica, name="pregunta_practica"),
    path("practicar/resultado/", practica_views.resultado_practica, name="resultado_practica"),

    path("juego/", juego_views.configurar_juego, name="juego_configurar",),
    path("juego/tablero/", juego_views.tablero_juego, name="juego_tablero",),
    path("juego/pregunta/", juego_views.pregunta_juego, name="juego_pregunta",),
    path("juego/resultado/", juego_views.resultado_juego, name="juego_resultado",),

    path("importacion/", importacion_views.importar_vocabulario, name="importar_vocabulario",),

    path("grupos/", grupo_views.listado_grupos, name="listado_grupos"),
    path("grupos/nuevo/", grupo_views.crear_grupo, name="crear_grupo"),
    path("grupos/invitaciones/", grupo_views.mis_invitaciones, name="mis_invitaciones",),
    path("grupos/invitaciones/<int:invitacion_id>/aceptar/", grupo_views.aceptar_invitacion, name="aceptar_invitacion",),
    path("grupos/invitaciones/<int:invitacion_id>/rechazar/", grupo_views.rechazar_invitacion, name="rechazar_invitacion",),
    path("grupos/<int:grupo_id>/salir/", grupo_views.salir_grupo, name="salir_grupo",),
    path("grupos/<int:grupo_id>/", grupo_views.detalle_grupo, name="detalle_grupo",),
    path("grupos/<int:grupo_id>/invitar/", grupo_views.invitar_usuario_grupo, name="invitar_usuario_grupo",),
    path("grupos/<int:grupo_id>/diccionarios/<int:diccionario_id>/", grupo_views.detalle_diccionario_grupo, name="detalle_diccionario_grupo",),
    path("grupos/<int:grupo_id>/diccionarios/nuevo/", grupo_views.crear_diccionario_grupo, name="crear_diccionario_grupo",),
    path("grupos/<int:grupo_id>/diccionarios/<int:diccionario_id>/temas/nuevo/", grupo_views.crear_tema_diccionario_grupo, name="crear_tema_diccionario_grupo",),
    path("grupos/<int:grupo_id>/diccionarios/<int:diccionario_id>/entradas/nuevo/", grupo_views.crear_entrada_diccionario_grupo, name="crear_entrada_diccionario_grupo",),

    path("grupos/<int:grupo_id>/diccionarios/<int:diccionario_id>/importar/", grupo_views.importar_vocabulario_diccionario_grupo, name="importar_vocabulario_diccionario_grupo",),
    path("grupos/<int:grupo_id>/diccionarios/<int:diccionario_id>/jugar/", grupo_views.jugar_diccionario_grupo, name="jugar_diccionario_grupo",),

    path("estadisticas/", estadistica_views.mis_estadisticas, name="mis_estadisticas",),
    path("estadisticas/dificiles/", estadistica_views.palabras_dificiles, name="palabras_dificiles",),
    path("estadisticas/repasar/", estadistica_views.repasar_dificiles, name="repasar_dificiles",),
    path("estadisticas/dificiles/jugar/", estadistica_views.jugar_dificiles, name="jugar_dificiles",),
]