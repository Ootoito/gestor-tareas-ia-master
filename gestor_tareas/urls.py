from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login_gestor_tareas, name="login_gestor_tareas"),
    path("", views.gestor_tareas_home, name="gestor_tareas_home"),
    path("nueva/", views.nueva_tarea, name="nueva_tarea"),
    path("cambiar-estado/<int:tarea_id>/", views.cambiar_estado, name="cambiar_estado"),
    path("eliminar/<int:tarea_id>/", views.eliminar_tarea, name="eliminar_tarea"),
    path("detalle/<int:tarea_id>/", views.detalle_tarea, name="detalle_tarea"),
    path("listado/", views.listado_tareas, name="listado_tareas"),
    path("nuevo-ambito/", views.nuevo_ambito, name="nuevo_ambito"),
    path("nuevo-tecnico/", views.nuevo_tecnico, name="nuevo_tecnico"),
    path("descartar-alerta/<int:id_alerta>/", views.descartar_alerta, name="descartar_alerta"),
    path("cambiar-grupo/", views.cambiar_grupo, name="cambiar_grupo"),
    path("nueva/", views.nueva_tarea, name="nueva_tarea"),
    path("anadir-nota/<int:tarea_id>/", views.anadir_nota, name="anadir_nota"),
    path("dashboard/", views.dashboard_gestor, name="dashboard_gestor"),
    path("admin-gestor/", views.admin_gestor, name="admin_gestor"),
    path("subtarea/<int:id_subtarea>/toggle/", views.toggle_subtarea, name="toggle_subtarea"),
    path("subtarea/<int:id_subtarea>/eliminar/", views.eliminar_subtarea, name="eliminar_subtarea"),
    path("mi-perfil/", views.mi_perfil, name="mi_perfil"),
]