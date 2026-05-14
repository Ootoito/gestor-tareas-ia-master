from django.contrib import admin
from .models import (
    GrupoTrabajo,
    UsuarioGestor,
    UsuarioGrupo,
    RolGestor,
    UsuarioRolGestor,
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