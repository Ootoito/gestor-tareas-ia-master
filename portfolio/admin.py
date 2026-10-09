from django.contrib import admin

from .models import Proyecto


@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):

    list_display = (
        "titulo",
        "estado",
        "destacado",
        "orden",
        "fecha_modificacion",
    )

    list_filter = (
        "estado",
        "destacado",
    )

    search_fields = (
        "titulo",
        "descripcion_corta",
        "descripcion",
        "tecnologias",
    )

    prepopulated_fields = {
        "slug": ("titulo",)
    }

    ordering = (
        "orden",
        "titulo",
    )