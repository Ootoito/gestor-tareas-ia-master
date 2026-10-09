from django.db import models


class Proyecto(models.Model):

    ESTADOS = [
        ("desarrollo", "En desarrollo"),
        ("finalizado", "Finalizado"),
        ("mantenimiento", "En mantenimiento"),
    ]

    titulo = models.CharField(
        max_length=150
    )

    slug = models.SlugField(
        max_length=160,
        unique=True
    )

    descripcion_corta = models.CharField(
        max_length=250
    )

    descripcion = models.TextField(
        blank=True
    )

    imagen = models.ImageField(
        upload_to="portfolio/proyectos/",
        blank=True,
        null=True
    )

    tecnologias = models.CharField(
        max_length=300,
        blank=True
    )

    url_proyecto = models.URLField(
        blank=True
    )

    url_github = models.URLField(
        blank=True
    )

    estado = models.CharField(
        max_length=20,
        choices=ESTADOS,
        default="desarrollo"
    )

    destacado = models.BooleanField(
        default=False
    )

    orden = models.PositiveIntegerField(
        default=0
    )

    fecha_creacion = models.DateTimeField(
        auto_now_add=True
    )

    fecha_modificacion = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ["orden", "-fecha_creacion"]

    def __str__(self):
        return self.titulo

    @property
    def tecnologias_lista(self):

        if not self.tecnologias:
            return []

        return [
            tecnologia.strip()
            for tecnologia in self.tecnologias.split(",")
            if tecnologia.strip()
        ]