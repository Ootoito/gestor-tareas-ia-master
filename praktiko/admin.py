from django.contrib import admin

from .models import (
    Diccionario,
    Tema,
    EntradaDiccionario,
    SesionPractica,
    RespuestaPractica,
    GrupoAprendizaje,
    MiembroGrupoAprendizaje,
    InvitacionGrupoAprendizaje,
)


@admin.register(Diccionario)
class DiccionarioAdmin(admin.ModelAdmin):
    list_display = (
        "icono",
        "nombre",
        "usuario",
        "grupo",
        "idioma_origen",
        "idioma_destino",
        "activo",
        "creado_en",
    )

    list_filter = (
        "activo",
        "grupo",
        "idioma_origen",
        "idioma_destino",
    )

    search_fields = (
        "nombre",
        "usuario__username",
        "grupo__nombre",
        "idioma_origen",
    )

@admin.register(Tema)
class TemaAdmin(admin.ModelAdmin):
    list_display = (
        "icono",
        "nombre",
        "color",
        "diccionario",
        "usuario",
        "activo",
    )

    list_filter = (
        "activo",
        "diccionario",
    )

    search_fields = (
        "nombre",
        "diccionario__nombre",
        "usuario__username",
    )


@admin.register(EntradaDiccionario)
class EntradaDiccionarioAdmin(admin.ModelAdmin):
    list_display = (
        "tipo",
        "texto_origen",
        "texto_destino",
        "diccionario",
        "tema",
        "usuario",
        "nivel",
        "activa",
    )
    list_filter = (
        "tipo",
        "nivel",
        "activa",
        "diccionario",
        "tema",
    )
    search_fields = (
        "texto_origen",
        "texto_destino",
        "usuario__username",
        "diccionario__nombre",
        "tema__nombre",
    )


@admin.register(SesionPractica)
class SesionPracticaAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "usuario",
        "diccionario",
        "tema",
        "total_tarjetas",
        "aciertos",
        "fallos",
        "porcentaje_acierto",
        "iniciada_en",
    )
    list_filter = ("diccionario", "tema", "usuario")
    search_fields = ("usuario__username", "diccionario__nombre")


@admin.register(RespuestaPractica)
class RespuestaPracticaAdmin(admin.ModelAdmin):
    list_display = (
        "sesion",
        "entrada",
        "respuesta_elegida",
        "respuesta_correcta",
        "correcta",
        "respondida_en",
    )
    list_filter = ("correcta",)
    search_fields = (
        "entrada__texto_origen",
        "entrada__texto_destino",
        "respuesta_elegida",
    )

@admin.register(GrupoAprendizaje)
class GrupoAprendizajeAdmin(admin.ModelAdmin):
    list_display = ("nombre", "creador", "activo", "creado_en")
    list_filter = ("activo",)
    search_fields = ("nombre", "creador__username")


@admin.register(MiembroGrupoAprendizaje)
class MiembroGrupoAprendizajeAdmin(admin.ModelAdmin):
    list_display = ("grupo", "usuario", "rol", "activo", "unido_en")
    list_filter = ("rol", "activo")
    search_fields = ("grupo__nombre", "usuario__username")


@admin.register(InvitacionGrupoAprendizaje)
class InvitacionGrupoAprendizajeAdmin(admin.ModelAdmin):
    list_display = ("grupo", "email", "invitado", "invitado_por", "estado", "creada_en")
    list_filter = ("estado",)
    search_fields = ("grupo__nombre", "email", "invitado__username")