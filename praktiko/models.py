from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Diccionario(models.Model):
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="praktiko_diccionarios",
    )

    nombre = models.CharField(max_length=100)
    idioma_origen = models.CharField(max_length=50)
    idioma_destino = models.CharField(max_length=50, default="Español")

    icono = models.CharField(
        max_length=10,
        blank=True,
        default="📚",
        help_text="Emoji o icono visual del diccionario. Ejemplo: 🇷🇺, 🇬🇧, 📚",
    )

    color = models.CharField(
        max_length=20,
        blank=True,
        default="#2563eb",
        help_text="Color principal del diccionario en formato hexadecimal.",
    )

    descripcion = models.TextField(blank=True)
    activo = models.BooleanField(default=True)
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    grupo = models.ForeignKey(
        "GrupoAprendizaje",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="diccionarios",
    )

    class Meta:
        verbose_name = "Diccionario"
        verbose_name_plural = "Diccionarios"
        ordering = ["nombre"]
        unique_together = ("usuario", "nombre")

    def __str__(self):
        return f"{self.nombre} ({self.usuario})"

    @property
    def es_compartido(self):
        return self.grupo_id is not None


class Tema(models.Model):
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="praktiko_temas",
    )
    diccionario = models.ForeignKey(
        Diccionario,
        on_delete=models.CASCADE,
        related_name="temas",
    )
    nombre = models.CharField(max_length=100)
    icono = models.CharField(
        max_length=10,
        blank=True,
        default="📁",
    )

    color = models.CharField(
        max_length=20,
        blank=True,
        default="#64748b",
    )

    orden = models.PositiveIntegerField(default=0)
    descripcion = models.TextField(blank=True)
    activo = models.BooleanField(default=True)
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Tema"
        verbose_name_plural = "Temas"
        ordering = ["nombre"]
        unique_together = ("usuario", "diccionario", "nombre")

    def __str__(self):
        return f"{self.nombre} - {self.diccionario.nombre}"


class EntradaDiccionario(models.Model):
    TIPO_PALABRA = "palabra"
    TIPO_FRASE = "frase"

    TIPO_CHOICES = [
        (TIPO_PALABRA, "Palabra"),
        (TIPO_FRASE, "Frase"),
    ]
    NIVEL_INICIAL = "inicial"
    NIVEL_BASICO = "basico"
    NIVEL_INTERMEDIO = "intermedio"
    NIVEL_AVANZADO = "avanzado"

    NIVEL_CHOICES = [
        (NIVEL_INICIAL, "Inicial"),
        (NIVEL_BASICO, "Básico"),
        (NIVEL_INTERMEDIO, "Intermedio"),
        (NIVEL_AVANZADO, "Avanzado"),
    ]

    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="praktiko_entradas",
    )
    diccionario = models.ForeignKey(
        Diccionario,
        on_delete=models.CASCADE,
        related_name="entradas",
    )
    tema = models.ForeignKey(
        Tema,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="entradas",
    )
    tipo = models.CharField(
        max_length=20,
        choices=TIPO_CHOICES,
        default=TIPO_PALABRA,
    )
    texto_origen = models.CharField(max_length=255)
    texto_destino = models.CharField(max_length=255)

    ejemplo_origen = models.TextField(blank=True)
    ejemplo_destino = models.TextField(blank=True)
    notas = models.TextField(blank=True)

    nivel = models.CharField(
        max_length=20,
        choices=NIVEL_CHOICES,
        default=NIVEL_INICIAL,
    )

    veces_practicada = models.PositiveIntegerField(default=0)
    veces_acertada = models.PositiveIntegerField(default=0)
    veces_fallada = models.PositiveIntegerField(default=0)

    ultima_practica = models.DateTimeField(null=True, blank=True)
    proxima_revision = models.DateTimeField(null=True, blank=True)

    activa = models.BooleanField(default=True)
    creada_en = models.DateTimeField(auto_now_add=True)
    actualizada_en = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Entrada de diccionario"
        verbose_name_plural = "Entradas de diccionario"
        ordering = ["texto_origen"]
        indexes = [
            models.Index(fields=["usuario", "diccionario"]),
            models.Index(fields=["usuario", "tema"]),
            models.Index(fields=["usuario", "nivel"]),
        ]

    @property
    def porcentaje_acierto(self):
        if self.veces_practicada == 0:
            return 0
        return round((self.veces_acertada / self.veces_practicada) * 100, 2)

    @property
    def es_dificil(self):
        return self.veces_practicada >= 3 and self.porcentaje_acierto < 60

    def registrar_respuesta(self, correcta):
        self.veces_practicada += 1
        self.ultima_practica = timezone.now()

        if correcta:
            self.veces_acertada += 1
        else:
            self.veces_fallada += 1

        self.save(
            update_fields=[
                "veces_practicada",
                "veces_acertada",
                "veces_fallada",
                "ultima_practica",
            ]
        )

    def __str__(self):
        return f"{self.texto_origen} → {self.texto_destino}"


class SesionPractica(models.Model):
    MODO_TEMA = "tema"
    MODO_DIFICILES = "dificiles"
    MODO_FALLADAS = "falladas"
    MODO_ALEATORIO = "aleatorio"

    MODO_CHOICES = [
        (MODO_TEMA, "Por tema"),
        (MODO_DIFICILES, "Palabras difíciles"),
        (MODO_FALLADAS, "Palabras falladas"),
        (MODO_ALEATORIO, "Aleatorio"),
    ]

    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="praktiko_sesiones",
    )
    diccionario = models.ForeignKey(
        Diccionario,
        on_delete=models.CASCADE,
        related_name="sesiones_practica",
    )
    tema = models.ForeignKey(
        Tema,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="sesiones_practica",
    )

    modo = models.CharField(
        max_length=20,
        choices=MODO_CHOICES,
        default=MODO_TEMA,
    )

    total_tarjetas = models.PositiveIntegerField(default=0)
    aciertos = models.PositiveIntegerField(default=0)
    fallos = models.PositiveIntegerField(default=0)

    iniciada_en = models.DateTimeField(auto_now_add=True)
    finalizada_en = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = "Sesión de práctica"
        verbose_name_plural = "Sesiones de práctica"
        ordering = ["-iniciada_en"]
        indexes = [
            models.Index(fields=["usuario", "diccionario"]),
            models.Index(fields=["usuario", "iniciada_en"]),
        ]

    @property
    def porcentaje_acierto(self):
        if self.total_tarjetas == 0:
            return 0
        return round((self.aciertos / self.total_tarjetas) * 100, 2)

    def finalizar(self):
        self.finalizada_en = timezone.now()
        self.save(update_fields=["finalizada_en"])

    def __str__(self):
        return f"Sesión {self.id} - {self.usuario}"


class RespuestaPractica(models.Model):
    EVALUACION_ERROR = "error"
    EVALUACION_DIFICIL = "dificil"
    EVALUACION_CORRECTO = "correcto"
    EVALUACION_FACIL = "facil"

    EVALUACION_CHOICES = [
        (EVALUACION_ERROR, "Error"),
        (EVALUACION_DIFICIL, "Difícil"),
        (EVALUACION_CORRECTO, "Correcto"),
        (EVALUACION_FACIL, "Fácil"),
    ]

    sesion = models.ForeignKey(
        SesionPractica,
        on_delete=models.CASCADE,
        related_name="respuestas",
    )
    entrada = models.ForeignKey(
        EntradaDiccionario,
        on_delete=models.CASCADE,
        related_name="respuestas_practica",
    )

    texto_origen = models.CharField(max_length=255)
    respuesta_elegida = models.CharField(max_length=255)
    respuesta_correcta = models.CharField(max_length=255)
    correcta = models.BooleanField(default=False)
    evaluacion = models.CharField(
        max_length=20,
        choices=EVALUACION_CHOICES,
        default=EVALUACION_CORRECTO,
    )
    respondida_en = models.DateTimeField(auto_now_add=True)

    
    class Meta:
        verbose_name = "Respuesta de práctica"
        verbose_name_plural = "Respuestas de práctica"
        ordering = ["respondida_en"]
        indexes = [
            models.Index(fields=["correcta"]),
            models.Index(fields=["respondida_en"]),
        ]

    def __str__(self):
        estado = "Correcta" if self.correcta else "Fallida"
        return f"{estado}: {self.texto_origen}"


class Examen(models.Model):
    TIPO_NORMAL = "normal"
    TIPO_OFICIAL = "oficial"
    TIPO_NIVEL = "nivel"
    TIPO_GRUPO = "grupo"
    TIPO_IA = "ia"

    TIPO_CHOICES = [
        (TIPO_NORMAL, "Normal"),
        (TIPO_OFICIAL, "Oficial"),
        (TIPO_NIVEL, "Nivel"),
        (TIPO_GRUPO, "Grupo"),
        (TIPO_IA, "IA"),
    ]

    SENTIDO_ORIGEN_DESTINO = "origen_destino"
    SENTIDO_DESTINO_ORIGEN = "destino_origen"
    SENTIDO_MIXTO = "mixto"

    SENTIDO_CHOICES = [
        (SENTIDO_ORIGEN_DESTINO, "Origen → destino"),
        (SENTIDO_DESTINO_ORIGEN, "Destino → origen"),
        (SENTIDO_MIXTO, "Mixto"),
    ]

    ESTADO_EN_CURSO = "en_curso"
    ESTADO_FINALIZADO = "finalizado"
    ESTADO_CANCELADO = "cancelado"

    ESTADO_CHOICES = [
        (ESTADO_EN_CURSO, "En curso"),
        (ESTADO_FINALIZADO, "Finalizado"),
        (ESTADO_CANCELADO, "Cancelado"),
    ]

    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="praktiko_examenes",
    )

    diccionario = models.ForeignKey(
        Diccionario,
        on_delete=models.CASCADE,
        related_name="examenes",
    )

    tema = models.ForeignKey(
        Tema,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="examenes",
    )

    tipo = models.CharField(
        max_length=20,
        choices=TIPO_CHOICES,
        default=TIPO_NORMAL,
    )

    sentido = models.CharField(
        max_length=30,
        choices=SENTIDO_CHOICES,
        default=SENTIDO_MIXTO,
    )

    numero_preguntas = models.PositiveIntegerField(default=15)
    aciertos = models.PositiveIntegerField(default=0)
    fallos = models.PositiveIntegerField(default=0)

    porcentaje = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0,
    )

    nota = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        default=0,
    )

    tiempo_segundos = models.PositiveIntegerField(default=0)

    estado = models.CharField(
        max_length=20,
        choices=ESTADO_CHOICES,
        default=ESTADO_EN_CURSO,
    )

    iniciada_en = models.DateTimeField(auto_now_add=True)
    finalizada_en = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = "Examen"
        verbose_name_plural = "Exámenes"
        ordering = ["-iniciada_en"]
        indexes = [
            models.Index(fields=["usuario", "iniciada_en"]),
            models.Index(fields=["usuario", "estado"]),
            models.Index(fields=["diccionario", "tema"]),
        ]

    @property
    def total_respuestas(self):
        return self.aciertos + self.fallos

    def finalizar(self):
        respuestas = self.respuestas.all()
        total_respuestas = respuestas.count()
        aciertos = respuestas.filter(correcta=True).count()
        fallos = total_respuestas - aciertos

        self.aciertos = aciertos
        self.fallos = fallos

        if total_respuestas > 0:
            self.porcentaje = round(
                (aciertos / total_respuestas) * 100,
                2,
            )
            self.nota = round(
                (aciertos / total_respuestas) * 10,
                2,
            )
        else:
            self.porcentaje = 0
            self.nota = 0

        self.finalizada_en = timezone.now()
        self.tiempo_segundos = max(
            0,
            int((self.finalizada_en - self.iniciada_en).total_seconds()),
        )
        self.estado = self.ESTADO_FINALIZADO

        self.save(
            update_fields=[
                "aciertos",
                "fallos",
                "porcentaje",
                "nota",
                "tiempo_segundos",
                "finalizada_en",
                "estado",
            ]
        )

    def __str__(self):
        return f"Examen {self.id} - {self.usuario}"


class RespuestaExamen(models.Model):
    examen = models.ForeignKey(
        Examen,
        on_delete=models.CASCADE,
        related_name="respuestas",
    )

    entrada = models.ForeignKey(
        EntradaDiccionario,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="respuestas_examen",
    )

    tema = models.ForeignKey(
        Tema,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="respuestas_examen",
    )

    sentido = models.CharField(
        max_length=30,
        choices=Examen.SENTIDO_CHOICES,
    )

    texto_pregunta = models.CharField(max_length=255)
    respuesta_usuario = models.CharField(max_length=255, blank=True)
    respuesta_correcta = models.CharField(max_length=255)

    correcta = models.BooleanField(default=False)
    orden = models.PositiveIntegerField()

    respondida_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Respuesta de examen"
        verbose_name_plural = "Respuestas de examen"
        ordering = ["orden"]
        unique_together = ("examen", "orden")
        indexes = [
            models.Index(fields=["examen", "correcta"]),
            models.Index(fields=["tema"]),
            models.Index(fields=["respondida_en"]),
        ]

    def __str__(self):
        estado = "Correcta" if self.correcta else "Fallida"
        return f"{estado}: {self.texto_pregunta}"

class GrupoAprendizaje(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField(blank=True)

    creador = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="praktiko_grupos_creados",
    )

    activo = models.BooleanField(default=True)
    creado_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Grupo de aprendizaje"
        verbose_name_plural = "Grupos de aprendizaje"
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre


class MiembroGrupoAprendizaje(models.Model):
    ROL_ADMIN = "admin"
    ROL_MIEMBRO = "miembro"

    ROL_CHOICES = [
        (ROL_ADMIN, "Administrador"),
        (ROL_MIEMBRO, "Miembro"),
    ]

    grupo = models.ForeignKey(
        GrupoAprendizaje,
        on_delete=models.CASCADE,
        related_name="miembros",
    )

    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="praktiko_grupos_miembro",
    )

    rol = models.CharField(
        max_length=20,
        choices=ROL_CHOICES,
        default=ROL_MIEMBRO,
    )

    activo = models.BooleanField(default=True)
    unido_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Miembro de grupo"
        verbose_name_plural = "Miembros de grupo"
        unique_together = ("grupo", "usuario")

    def __str__(self):
        return f"{self.usuario.username} - {self.grupo.nombre}"


class InvitacionGrupoAprendizaje(models.Model):
    ESTADO_PENDIENTE = "pendiente"
    ESTADO_ACEPTADA = "aceptada"
    ESTADO_RECHAZADA = "rechazada"

    ESTADO_CHOICES = [
        (ESTADO_PENDIENTE, "Pendiente"),
        (ESTADO_ACEPTADA, "Aceptada"),
        (ESTADO_RECHAZADA, "Rechazada"),
    ]

    grupo = models.ForeignKey(
        GrupoAprendizaje,
        on_delete=models.CASCADE,
        related_name="invitaciones",
    )

    invitado = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="praktiko_invitaciones_recibidas",
    )

    invitado_por = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="praktiko_invitaciones_enviadas",
    )

    email = models.EmailField()

    estado = models.CharField(
        max_length=20,
        choices=ESTADO_CHOICES,
        default=ESTADO_PENDIENTE,
    )

    creada_en = models.DateTimeField(auto_now_add=True)
    respondida_en = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = "Invitación a grupo"
        verbose_name_plural = "Invitaciones a grupos"

    def __str__(self):
        return f"{self.email} - {self.grupo.nombre} - {self.estado}"


class EstadisticaEntradaUsuario(models.Model):
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="praktiko_estadisticas_entradas",
    )

    entrada = models.ForeignKey(
        EntradaDiccionario,
        on_delete=models.CASCADE,
        related_name="estadisticas_usuario",
    )

    veces_preguntada = models.PositiveIntegerField(default=0)
    aciertos = models.PositiveIntegerField(default=0)
    fallos = models.PositiveIntegerField(default=0)

    ultimo_acierto = models.DateTimeField(null=True, blank=True)
    ultimo_fallo = models.DateTimeField(null=True, blank=True)

    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Estadística de entrada por usuario"
        verbose_name_plural = "Estadísticas de entradas por usuario"
        unique_together = ("usuario", "entrada")
        ordering = ["-fallos", "-veces_preguntada"]

    def __str__(self):
        return f"{self.usuario} - {self.entrada}"
    
    @property
    def porcentaje_acierto(self):
        if self.veces_preguntada == 0:
            return 0

        return round(
            (self.aciertos / self.veces_preguntada) * 100,
            2,
        )