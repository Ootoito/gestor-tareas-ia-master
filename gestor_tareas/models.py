from django.db import models
from django.contrib.auth.models import User


class GrupoTrabajo(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    activo = models.BooleanField(default=True)

    class Meta:
        db_table = "gestor_tareas_tbgrupos"
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre


class UsuarioGestor(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="perfil_gestor",
    )
    alias = models.CharField(max_length=100, blank=True, null=True)
    activo = models.BooleanField(default=True)
    es_admin_gestor = models.BooleanField(default=False)

    class Meta:
        db_table = "gestor_tareas_tbusuarios"
        ordering = ["user__username"]

    def __str__(self):
        return self.alias or self.user.username


class UsuarioGrupo(models.Model):
    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="grupos_gestor",
    )
    grupo = models.ForeignKey(
        GrupoTrabajo,
        on_delete=models.CASCADE,
        related_name="usuarios",
    )
    activo = models.BooleanField(default=True)

    class Meta:
        db_table = "gestor_tareas_tbusuarios_grupos"
        unique_together = ("usuario", "grupo")
        ordering = ["grupo__nombre", "usuario__username"]

    def __str__(self):
        return f"{self.usuario.username} -> {self.grupo.nombre}"
    
class RolGestor(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.CharField(max_length=200, blank=True, null=True)
    activo = models.BooleanField(default=True)

    class Meta:
        db_table = "gestor_tareas_tbroles"
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre


class UsuarioRolGestor(models.Model):
    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="roles_gestor",
    )
    rol = models.ForeignKey(
        RolGestor,
        on_delete=models.CASCADE,
        related_name="usuarios",
    )
    activo = models.BooleanField(default=True)

    class Meta:
        db_table = "gestor_tareas_tbusuarios_roles"
        unique_together = ("usuario", "rol")
        ordering = ["usuario__username", "rol__nombre"]

    def __str__(self):
        return f"{self.usuario.username} -> {self.rol.nombre}"
    
class EstadoTarea(models.Model):
    id_estado = models.AutoField(primary_key=True)

    nombre = models.CharField(max_length=100, unique=True)

    orden = models.PositiveIntegerField(default=0)

    activo = models.BooleanField(default=True)

    class Meta:
        db_table = "gestor_tareas_tbestados"
        ordering = ["orden", "nombre"]

    def __str__(self):
        return self.nombre


class AmbitoTarea(models.Model):
    id_ambito = models.AutoField(primary_key=True)

    nombre = models.CharField(max_length=150, unique=True)

    activo = models.BooleanField(default=True)

    class Meta:
        db_table = "gestor_tareas_tbambitos"
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre


class Tecnico(models.Model):
    id_tecnico = models.AutoField(primary_key=True)

    nombre = models.CharField(max_length=150, unique=True)

    activo = models.BooleanField(default=True)

    class Meta:
        db_table = "gestor_tareas_tbtecnicos"
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre


class TecnicoGrupo(models.Model):

    tecnico = models.ForeignKey(
        Tecnico,
        on_delete=models.CASCADE,
        related_name="grupos",
        db_column="id_tecnico",
    )

    grupo = models.ForeignKey(
        GrupoTrabajo,
        on_delete=models.CASCADE,
        related_name="tecnicos",
        db_column="id_grupo",
    )

    activo = models.BooleanField(default=True)

    class Meta:
        db_table = "gestor_tareas_tbtecnicos_grupos"
        ordering = ["grupo__nombre", "tecnico__nombre"]

    def __str__(self):
        return f"{self.tecnico.nombre} -> {self.grupo.nombre}"

    
class Tarea(models.Model):
    id = models.BigAutoField(primary_key=True)

    numero_tarea = models.IntegerField()

    fecha = models.DateField()

    estado = models.ForeignKey(
        EstadoTarea,
        on_delete=models.PROTECT,
        db_column="id_estado",
        related_name="tareas",
    )

    prioridad = models.CharField(max_length=20, default="Normal")

    ambito = models.ForeignKey(
        AmbitoTarea,
        on_delete=models.PROTECT,
        db_column="id_ambito",
        related_name="tareas",
        null=True,
        blank=True,
    )

    tecnico = models.ForeignKey(
        Tecnico,
        on_delete=models.SET_NULL,
        db_column="id_tecnico",
        related_name="tareas",
        null=True,
        blank=True,
    )

    grupo = models.ForeignKey(
        GrupoTrabajo,
        on_delete=models.PROTECT,
        db_column="id_grupo",
        related_name="tareas",
    )

    titulo = models.CharField(max_length=300)

    descripcion = models.TextField(null=True, blank=True)

    usuario_creador = models.CharField(max_length=100, null=True, blank=True)

    usuario_asignado = models.CharField(max_length=100, null=True, blank=True)

    activa = models.BooleanField(default=True)

    fecha_creacion = models.DateTimeField(auto_now_add=True)

    fecha_objetivo = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "gestor_tareas_tbtareas"
        ordering = ["-fecha_creacion", "-id"]

    def __str__(self):
        return f"{self.numero_tarea} - {self.titulo}"


class NotaTarea(models.Model):
    id_nota = models.BigAutoField(primary_key=True)

    tarea = models.ForeignKey(
        Tarea,
        on_delete=models.CASCADE,
        db_column="id_tarea",
        related_name="notas",
    )

    fecha = models.DateTimeField(auto_now_add=True)

    usuario = models.CharField(max_length=100, null=True, blank=True)

    texto = models.TextField()

    activa = models.BooleanField(default=True)

    class Meta:
        db_table = "gestor_tareas_tbnotas"
        ordering = ["-fecha"]

    def __str__(self):
        return f"Nota {self.id_nota} - Tarea {self.tarea_id}"