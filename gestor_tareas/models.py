from django.db import models
from django.contrib.auth.models import User


class GrupoTrabajo(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    activo = models.BooleanField(default=True)

    class Meta:
        db_table = "gestor_tareas_tbgrupos"
        verbose_name = "Grupo de trabajo"
        verbose_name_plural = "Grupos de trabajo"
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
        verbose_name = "Usuario del gestor"
        verbose_name_plural = "Usuarios del gestor"
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
        verbose_name = "Relación usuario-grupo"
        verbose_name_plural = "Relaciones usuario-grupo"
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
        verbose_name = "Rol del gestor"
        verbose_name_plural = "Roles del gestor"
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
        verbose_name = "Relación usuario-rol"
        verbose_name_plural = "Relaciones usuario-rol"
        unique_together = ("usuario", "rol")
        ordering = ["usuario__username", "rol__nombre"]

    def __str__(self):
        return f"{self.usuario.username} -> {self.rol.nombre}"