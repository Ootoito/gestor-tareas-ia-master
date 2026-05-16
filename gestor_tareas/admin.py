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
    list_display = ("id", "nombre", "grupo", "color_clase", "orden", "activo")
    list_filter = ("activo", "grupo")
    search_fields = ("nombre", "grupo__nombre")
    ordering = ("grupo", "orden", "nombre")


@admin.register(AmbitoTarea)
class AmbitoTareaAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "grupo", "activo")
    list_filter = ("activo", "grupo")
    search_fields = ("nombre", "grupo__nombre")


@admin.register(Tecnico)
class TecnicoAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "activo")
    list_filter = ("activo",)
    search_fields = ("nombre",)


@admin.register(TecnicoGrupo)
class TecnicoGrupoAdmin(admin.ModelAdmin):
    list_display = ("id", "tecnico", "grupo", "activo")
    list_filter = ("activo", "grupo")
    search_fields = ("tecnico__nombre", "grupo__nombre")