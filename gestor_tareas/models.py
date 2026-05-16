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
    nombre = models.CharField(max_length=100)
    grupo = models.ForeignKey(
        GrupoTrabajo,
        on_delete=models.CASCADE,
        related_name="estados",
        null=True,
        blank=True,
    )
    color_clase = models.CharField(max_length=50, default="azul")
    orden = models.PositiveIntegerField(default=0)
    activo = models.BooleanField(default=True)

    class Meta:
        db_table = "gestor_tareas_tbestados"
        ordering = ["orden", "nombre"]
        unique_together = ("nombre", "grupo")

    def __str__(self):
        return self.nombre


class AmbitoTarea(models.Model):
    nombre = models.CharField(max_length=100)
    grupo = models.ForeignKey(
        GrupoTrabajo,
        on_delete=models.CASCADE,
        related_name="ambitos",
    )
    activo = models.BooleanField(default=True)

    class Meta:
        db_table = "gestor_tareas_tbambitos"
        ordering = ["nombre"]
        unique_together = ("nombre", "grupo")

    def __str__(self):
        return self.nombre


class Tecnico(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
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
    )
    grupo = models.ForeignKey(
        GrupoTrabajo,
        on_delete=models.CASCADE,
        related_name="tecnicos",
    )
    activo = models.BooleanField(default=True)

    class Meta:
        db_table = "gestor_tareas_tbtecnicos_grupos"
        ordering = ["grupo__nombre", "tecnico__nombre"]
        unique_together = ("tecnico", "grupo")

    def __str__(self):
        return f"{self.tecnico.nombre} -> {self.grupo.nombre}"