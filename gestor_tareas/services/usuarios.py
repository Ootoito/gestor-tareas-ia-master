from django.contrib.auth.models import User

from gestor_tareas.models import (
    UsuarioGestor,
    UsuarioGrupo,
    Tecnico,
    TecnicoGrupo,
    GrupoTrabajo,
)


def obtener_alias_usuario(user):
    perfil = UsuarioGestor.objects.filter(user=user).first()

    if perfil and perfil.alias:
        return perfil.alias

    return user.username


def sincronizar_usuario_como_tecnico_en_grupo(user, grupo):
    """
    Garantiza que un usuario pertenezca a un grupo y que exista como técnico
    asignable dentro de ese mismo grupo.
    """

    UsuarioGrupo.objects.update_or_create(
        usuario=user,
        grupo=grupo,
        defaults={"activo": True},
    )

    alias_tecnico = obtener_alias_usuario(user)

    tecnico, _ = Tecnico.objects.update_or_create(
        nombre=alias_tecnico,
        defaults={"activo": True},
    )

    TecnicoGrupo.objects.update_or_create(
        tecnico=tecnico,
        grupo=grupo,
        defaults={"activo": True},
    )

    return tecnico


def crear_o_actualizar_usuario_gestor(username, alias, password, id_grupo):
    """
    Crea o actualiza un usuario del gestor y lo asigna automáticamente
    como técnico del grupo indicado.
    """

    grupo = GrupoTrabajo.objects.get(id=id_grupo)

    user, creado = User.objects.get_or_create(
        username=username,
        defaults={"is_active": True},
    )

    if creado:
        if password:
            user.set_password(password)
        user.is_active = True
        user.save()
    elif password:
        user.set_password(password)
        user.is_active = True
        user.save()

    UsuarioGestor.objects.update_or_create(
        user=user,
        defaults={
            "alias": alias or username,
            "activo": True,
        },
    )

    sincronizar_usuario_como_tecnico_en_grupo(user, grupo)

    return user, grupo