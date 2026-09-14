from django.contrib import admin

from .models import Aeronave, ContenidoDCS, MisionDCS


class ContenidoInline(admin.TabularInline):
    model = ContenidoDCS

    extra = 0

    fields = (
        "titulo",
        "tipo",
        "estado",
        "activo",
        "orden",
    )

    show_change_link = True


@admin.register(Aeronave)
class AeronaveAdmin(admin.ModelAdmin):

    list_display = (
        "nombre",
        "slug",
        "activo",
        "orden",
    )

    list_filter = (
        "activo",
    )

    search_fields = (
        "nombre",
        "descripcion",
    )

    prepopulated_fields = {
        "slug": ("nombre",),
    }

    ordering = (
        "orden",
        "nombre",
    )

    inlines = [
        ContenidoInline,
    ]


class MisionInline(admin.TabularInline):
    model = MisionDCS

    extra = 0

    fields = (
        "numero",
        "titulo",
        "url_descarga",
        "activo",
        "orden",
    )

    ordering = (
        "orden",
        "numero",
    )


@admin.register(ContenidoDCS)
class ContenidoDCSAdmin(admin.ModelAdmin):

    list_display = (
        "titulo",
        "aeronave",
        "tipo",
        "estado",
        "activo",
        "orden",
    )

    list_filter = (
        "tipo",
        "estado",
        "activo",
        "aeronave",
    )

    search_fields = (
        "titulo",
        "descripcion",
        "situacion",
        "objetivo",
    )

    prepopulated_fields = {
        "slug": ("titulo",),
    }

    ordering = (
        "aeronave",
        "orden",
        "titulo",
    )

    inlines = [
        MisionInline,
    ]


@admin.register(MisionDCS)
class MisionDCSAdmin(admin.ModelAdmin):

    list_display = (
        "numero",
        "titulo",
        "contenido",
        "activo",
        "orden",
    )

    list_filter = (
        "activo",
        "contenido__aeronave",
        "contenido",
    )

    search_fields = (
        "titulo",
        "descripcion",
        "contenido__titulo",
        "contenido__aeronave__nombre",
    )

    ordering = (
        "contenido",
        "orden",
        "numero",
    )