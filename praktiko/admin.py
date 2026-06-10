from django.contrib import admin

from .models import (
    Diccionario,
    Tema,
    EntradaDiccionario,
    SesionPractica,
    RespuestaPractica,
)


@admin.register(Diccionario)
class DiccionarioAdmin(admin.ModelAdmin):
    list_display = (
        "icono",
        "nombre",
        "usuario",
        "idioma_origen",
        "idioma_destino",
        "color",
        "activo",
        "creado_en",
    )
    list_filter = ("activo", "idioma_origen", "idioma_destino")
    search_fields = ("nombre", "usuario__username", "idioma_origen")


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