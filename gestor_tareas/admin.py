from django.contrib import admin
from .models import (
    GrupoTrabajo,
    UsuarioGestor,
    UsuarioGrupo,
    RolGestor,
    UsuarioRolGestor,
    EstadoTarea,
    AmbitoTarea,
    Tecnico,
    TecnicoGrupo,
    Tarea,
    Tarea,
    NotaTarea,
)


@admin.register(GrupoTrabajo)
class GrupoTrabajoAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "activo")
    list_filter = ("activo",)
    search_fields = ("nombre",)


@admin.register(UsuarioGestor)
class UsuarioGestorAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "alias", "activo", "es_admin_gestor")
    list_filter = ("activo", "es_admin_gestor")
    search_fields = ("user__username", "alias")


@admin.register(UsuarioGrupo)
class UsuarioGrupoAdmin(admin.ModelAdmin):
    list_display = ("id", "usuario", "grupo", "activo")
    list_filter = ("activo", "grupo")
    search_fields = ("usuario__username", "grupo__nombre")


@admin.register(RolGestor)
class RolGestorAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "activo")
    list_filter = ("activo",)
    search_fields = ("nombre", "descripcion")


@admin.register(UsuarioRolGestor)
class UsuarioRolGestorAdmin(admin.ModelAdmin):
    list_display = ("id", "usuario", "rol", "activo")
    list_filter = ("activo", "rol")
    search_fields = ("usuario__username", "rol__nombre")

@admin.register(EstadoTarea)
class EstadoTareaAdmin(admin.ModelAdmin):
    list_display = ("id_estado", "nombre", "orden", "activo")
    list_filter = ("activo",)
    search_fields = ("nombre",)
    ordering = ("orden", "nombre")


@admin.register(AmbitoTarea)
class AmbitoTareaAdmin(admin.ModelAdmin):
    list_display = ("id_ambito", "nombre", "activo")
    list_filter = ("activo",)
    search_fields = ("nombre",)
    ordering = ("nombre",)


@admin.register(Tecnico)
class TecnicoAdmin(admin.ModelAdmin):
    list_display = ("id_tecnico", "nombre", "activo")
    list_filter = ("activo",)
    search_fields = ("nombre",)


@admin.register(TecnicoGrupo)
class TecnicoGrupoAdmin(admin.ModelAdmin):
    list_display = ("id", "tecnico", "grupo", "activo")
    list_filter = ("activo", "grupo")
    search_fields = ("tecnico__nombre", "grupo__nombre")

@admin.register(Tarea)
class TareaAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "numero_tarea",
        "titulo",
        "grupo",
        "estado",
        "prioridad",
        "ambito",
        "tecnico",
        "activa",
        "fecha_creacion",
        "fecha_objetivo",
    )
    list_filter = (
        "grupo",
        "estado",
        "prioridad",
        "ambito",
        "tecnico",
        "activa",
    )
    search_fields = (
        "titulo",
        "descripcion",
        "usuario_creador",
        "usuario_asignado",
    )
    ordering = ("-fecha_creacion", "-id")


@admin.register(NotaTarea)
class NotaTareaAdmin(admin.ModelAdmin):
    list_display = (
        "id_nota",
        "tarea",
        "usuario",
        "fecha",
        "activa",
    )
    list_filter = (
        "activa",
        "usuario",
    )
    search_fields = (
        "texto",
        "usuario",
        "tarea__titulo",
    )
    ordering = ("-fecha",)