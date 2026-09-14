from django.db import models


class Aeronave(models.Model):
    """
    Aeronaves o módulos de DCS World.

    Ejemplos:
    - F-4E Phantom II
    - Mirage F1
    - Mi-24P Hind
    """

    nombre = models.CharField(
        max_length=150,
        unique=True,
    )

    slug = models.SlugField(
        max_length=150,
        unique=True,
    )

    descripcion = models.TextField(
        blank=True,
    )

    imagen = models.CharField(
        max_length=255,
        blank=True,
        help_text=(
            "Ruta de la imagen dentro de static/dcs/. "
            "Ejemplo: imagenes/F4EPhantom.png"
        ),
    )

    activo = models.BooleanField(
        default=True,
    )

    orden = models.PositiveIntegerField(
        default=0,
    )

    class Meta:
        ordering = ["orden", "nombre"]
        verbose_name = "Aeronave"
        verbose_name_plural = "Aeronaves"

    def __str__(self):
        return self.nombre


class ContenidoDCS(models.Model):
    """
    Agrupación de misiones pertenecientes a una aeronave.

    Puede representar:
    - un curso
    - una campaña
    - una colección de misiones independientes
    """

    TIPO_CURSO = "curso"
    TIPO_CAMPANA = "campana"
    TIPO_MISIONES = "misiones"

    TIPOS = [
        (TIPO_CURSO, "Curso"),
        (TIPO_CAMPANA, "Campaña"),
        (TIPO_MISIONES, "Misiones"),
    ]

    ESTADO_PUBLICADO = "publicado"
    ESTADO_DESARROLLO = "desarrollo"
    ESTADO_OCULTO = "oculto"

    ESTADOS = [
        (ESTADO_PUBLICADO, "Publicado"),
        (ESTADO_DESARROLLO, "En desarrollo"),
        (ESTADO_OCULTO, "Oculto"),
    ]

    aeronave = models.ForeignKey(
        Aeronave,
        on_delete=models.CASCADE,
        related_name="contenidos",
    )

    titulo = models.CharField(
        max_length=200,
    )

    slug = models.SlugField(
        max_length=200,
    )

    tipo = models.CharField(
        max_length=20,
        choices=TIPOS,
        default=TIPO_MISIONES,
    )

    descripcion = models.TextField(
        blank=True,
    )

    situacion = models.TextField(
        blank=True,
    )

    objetivo = models.TextField(
        blank=True,
    )

    imagen = models.CharField(
        max_length=255,
        blank=True,
        help_text=(
            "Ruta de la imagen dentro de static/dcs/. "
            "Ejemplo: imagenes/fuegoenelestrecho.png"
        ),
    )

    estado = models.CharField(
        max_length=20,
        choices=ESTADOS,
        default=ESTADO_PUBLICADO,
    )

    activo = models.BooleanField(
        default=True,
    )

    orden = models.PositiveIntegerField(
        default=0,
    )

    class Meta:
        ordering = ["orden", "titulo"]

        constraints = [
            models.UniqueConstraint(
                fields=["aeronave", "slug"],
                name="dcs_contenido_aeronave_slug_unique",
            ),
        ]

        verbose_name = "Contenido DCS"
        verbose_name_plural = "Contenidos DCS"

    def __str__(self):
        return f"{self.aeronave.nombre} · {self.titulo}"


class MisionDCS(models.Model):
    """
    Una misión individual perteneciente a un curso,
    campaña o colección.
    """

    contenido = models.ForeignKey(
        ContenidoDCS,
        on_delete=models.CASCADE,
        related_name="misiones",
    )

    numero = models.PositiveIntegerField()

    titulo = models.CharField(
        max_length=250,
    )

    descripcion = models.TextField(
        blank=True,
    )

    url_descarga = models.URLField(
        max_length=500,
        blank=True,
    )

    activo = models.BooleanField(
        default=True,
    )

    orden = models.PositiveIntegerField(
        default=0,
    )

    class Meta:
        ordering = ["orden", "numero"]

        constraints = [
            models.UniqueConstraint(
                fields=["contenido", "numero"],
                name="dcs_mision_contenido_numero_unique",
            ),
        ]

        verbose_name = "Misión DCS"
        verbose_name_plural = "Misiones DCS"

    def __str__(self):
        return (
            f"{self.contenido.titulo} · "
            f"{self.numero:02d} · "
            f"{self.titulo}"
        )