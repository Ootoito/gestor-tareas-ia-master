from django.urls import path

from gestor_tareas.vistas import auth_views
from . import views
from .vistas import message_views, profile_views, auth_views, dashboard_views, subtask_views, alert_views, admin_views, task_views



urlpatterns = [
    path("login/", auth_views.login_gestor_tareas, name="login_gestor_tareas"),
    path("logout/", auth_views.logout_gestor_tareas, name="logout_gestor_tareas"),
    path("", views.gestor_tareas_home, name="gestor_tareas_home"),
    path("nueva/", views.nueva_tarea, name="nueva_tarea"),
    path("cambiar-estado/<int:tarea_id>/", views.cambiar_estado, name="cambiar_estado"),
    path("eliminar/<int:tarea_id>/", task_views.eliminar_tarea, name="eliminar_tarea"),
    path("detalle/<int:tarea_id>/", views.detalle_tarea, name="detalle_tarea"),
    path("listado/", views.listado_tareas, name="listado_tareas"),
    path("nuevo-ambito/", views.nuevo_ambito, name="nuevo_ambito"),
    path("nuevo-tecnico/", views.nuevo_tecnico, name="nuevo_tecnico"),
    path("descartar-alerta/<int:id_alerta>/", alert_views.descartar_alerta, name="descartar_alerta"),
    path("cambiar-grupo/", views.cambiar_grupo, name="cambiar_grupo"),
    path("nueva/", views.nueva_tarea, name="nueva_tarea"),
    path("anadir-nota/<int:tarea_id>/", task_views.anadir_nota, name="anadir_nota"),
    path("dashboard/", dashboard_views.dashboard_gestor, name="dashboard_gestor"),
    path("admin-gestor/", admin_views.admin_gestor, name="admin_gestor"),
    path("subtarea/<int:id_subtarea>/toggle/", subtask_views.toggle_subtarea, name="toggle_subtarea"),
    path("subtarea/<int:id_subtarea>/eliminar/", subtask_views.eliminar_subtarea, name="eliminar_subtarea"),
    path("mi-perfil/", profile_views.mi_perfil, name="mi_perfil"),    
    path("mensajes/", message_views.mensajes_gestor, name="mensajes_gestor"),
    path("mensajes/<int:id_mensaje>/", message_views.detalle_mensaje, name="detalle_mensaje"),
    path("mensajes/<int:id_mensaje>/leido/", message_views.marcar_mensaje_leido, name="marcar_mensaje_leido"),    
]