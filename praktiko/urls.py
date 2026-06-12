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
]