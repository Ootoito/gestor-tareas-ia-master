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

    # ---------------------------------------------------------
    # Imagen histórica
    # ---------------------------------------------------------
    # Mantiene compatibilidad con las imágenes que actualmente
    # forman parte de static/dcs/.
    #
    # Ejemplo:
    # imagenes/F4EPhantom.png
    #
    imagen = models.CharField(
        max_length=255,
        blank=True,
        help_text=(
            "Ruta de la imagen dentro de static/dcs/. "
            "Ejemplo: imagenes/F4EPhantom.png"
        ),
    )

    # ---------------------------------------------------------
    # Imagen subida desde el gestor
    # ---------------------------------------------------------
    # Las nuevas imágenes administradas desde la zona privada
    # se almacenarán en:
    #
    # MEDIA_ROOT/dcs/aeronaves/
    #
    imagen_subida = models.ImageField(
        upload_to="dcs/aeronaves/",
        blank=True,
        null=True,
        verbose_name="Imagen subida",
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

    @property
    def tiene_imagen_subida(self):
        """
        Indica si la aeronave dispone de una imagen
        almacenada mediante MEDIA.
        """
        return bool(self.imagen_subida)

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

    # ---------------------------------------------------------
    # Imagen histórica
    # ---------------------------------------------------------
    # Mantiene compatibilidad con las imágenes que actualmente
    # forman parte de static/dcs/.
    #
    # Ejemplo:
    # imagenes/fuegoenelestrecho.png
    #
    imagen = models.CharField(
        max_length=255,
        blank=True,
        help_text=(
            "Ruta de la imagen dentro de static/dcs/. "
            "Ejemplo: imagenes/fuegoenelestrecho.png"
        ),
    )

    # ---------------------------------------------------------
    # Imagen subida desde el gestor
    # ---------------------------------------------------------
    # Las nuevas imágenes administradas desde la zona privada
    # se almacenarán en:
    #
    # MEDIA_ROOT/dcs/contenidos/
    #
    imagen_subida = models.ImageField(
        upload_to="dcs/contenidos/",
        blank=True,
        null=True,
        verbose_name="Imagen subida",
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

    @property
    def tiene_imagen_subida(self):
        """
        Indica si el contenido dispone de una imagen
        almacenada mediante MEDIA.
        """
        return bool(self.imagen_subida)

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

    # ---------------------------------------------------------
    # URL histórica
    # ---------------------------------------------------------
    # Se mantiene para conservar compatibilidad con las misiones
    # ya importadas de F-4E y Mirage F1.
    #
    # Las nuevas misiones pueden utilizar VersionMisionDCS
    # cuando existan varias descargas para una misma misión.
    #
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

    @property
    def tiene_versiones(self):
        """
        Indica si la misión dispone de una o más versiones
        de descarga almacenadas en VersionMisionDCS.
        """
        return self.versiones.filter(activo=True).exists()

    def __str__(self):
        return (
            f"{self.contenido.titulo} · "
            f"{self.numero:02d} · "
            f"{self.titulo}"
        )


class VersionMisionDCS(models.Model):
    """
    Una versión descargable de una misión.

    Permite que una misma misión pueda disponer de varias
    variantes, por ejemplo:

    - Versión estándar
    - Versión nocturna
    - Versión con mal tiempo
    - Versión con escolta armada
    """

    mision = models.ForeignKey(
        MisionDCS,
        on_delete=models.CASCADE,
        related_name="versiones",
    )

    nombre = models.CharField(
        max_length=150,
        verbose_name="Nombre de la versión",
    )

    url_descarga = models.URLField(
        max_length=500,
        verbose_name="URL de descarga",
    )

    activo = models.BooleanField(
        default=True,
    )

    orden = models.PositiveIntegerField(
        default=0,
    )

    class Meta:
        ordering = ["orden", "id"]

        constraints = [
            models.UniqueConstraint(
                fields=["mision", "nombre"],
                name="dcs_version_mision_nombre_unique",
            ),
        ]

        verbose_name = "Versión de misión DCS"
        verbose_name_plural = "Versiones de misiones DCS"

    def __str__(self):
        return (
            f"{self.mision.contenido.titulo} · "
            f"{self.mision.numero:02d} · "
            f"{self.nombre}"
        )