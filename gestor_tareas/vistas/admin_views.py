from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import transaction
from django.shortcuts import redirect, render

from gestor_tareas.models import (
    GrupoTrabajo,
    EstadoTarea,
    AmbitoTarea,
    UsuarioGestor,
    UsuarioGrupo,
    Tecnico,
    TecnicoGrupo,
)

from gestor_tareas.vistas.common import usuario_es_admin_gestor

from gestor_tareas.services.usuarios import (
    crear_o_actualizar_usuario_gestor,
    sincronizar_usuario_como_tecnico_en_grupo,
)

@login_required
def admin_gestor(request):
    if not usuario_es_admin_gestor(request.user):
        messages.error(request, "No tienes permisos de administración del gestor.")
        return redirect("gestor_tareas_home")

    if request.method == "POST":
        accion = request.POST.get("accion", "").strip()

        if accion == "crear_grupo":
            nombre = request.POST.get("nombre_grupo", "").strip()

            if not nombre:
                messages.error(request, "Debes indicar el nombre del grupo.")
            else:
                grupo, creado = GrupoTrabajo.objects.get_or_create(
                    nombre=nombre,
                    defaults={"activo": True},
                )

                if creado:
                    EstadoTarea.objects.get_or_create(
                        grupo=grupo,
                        nombre="Pendiente",
                        defaults={
                            "orden": 1,
                            "color": "#2563eb",
                            "activo": True,
                        }
                    )

                    EstadoTarea.objects.get_or_create(
                        grupo=grupo,
                        nombre="Completada",
                        defaults={
                        "orden": 2,
                        "color": "#16a34a",
                        "activo": True,
                        }
                    )

                    AmbitoTarea.objects.get_or_create(
                        nombre="General",
                        defaults={
                            "activo": True,
                        }
                    )

                messages.success(request, "Grupo creado correctamente.")

        elif accion == "crear_usuario":

            username = request.POST.get("username", "").strip()
            alias = request.POST.get("alias", "").strip()
            password = request.POST.get("password", "").strip()
            id_grupo = request.POST.get("id_grupo", "").strip()

            if not username:
                messages.error(request, "Debes indicar el usuario.")
            elif not id_grupo:
                messages.error(request, "Debes seleccionar un grupo.")
            else:
                with transaction.atomic():

                    user, grupo = crear_o_actualizar_usuario_gestor(
                        username=username,
                        alias=alias,
                        password=password,
                        id_grupo=id_grupo,
                    )

                    if user == request.user:
                        request.session["gestor_tareas_id_grupo"] = grupo.id
                        request.session["gestor_tareas_grupo"] = grupo.nombre

                messages.success(
                    request,
                    "Usuario creado/asignado correctamente y añadido como técnico del grupo."
                )

        elif accion == "toggle_usuario":

            id_usuario = request.POST.get("id_usuario")

            try:
                perfil = UsuarioGestor.objects.get(id=id_usuario)

                perfil.activo = not perfil.activo
                perfil.save()

                perfil.user.is_active = perfil.activo
                perfil.user.save()

                if perfil.activo:
                    messages.success(request, f"{perfil.user.username} ha sido activado.")
                else:
                    messages.success(request, f"{perfil.user.username} ha sido desactivado.")

            except UsuarioGestor.DoesNotExist:
                messages.error(request, "Usuario no encontrado.")
        
        elif accion == "crear_estado":

            nombre_estado = request.POST.get("nombre_estado", "").strip()
            orden_estado = request.POST.get("orden_estado", "0").strip()
            color_estado = request.POST.get("color_estado", "#6c757d").strip() or "#6c757d"
            id_grupo_estado = request.POST.get("id_grupo_estado", "").strip()

            if not nombre_estado:
                messages.error(request, "Debes indicar el nombre del estado.")
            elif not id_grupo_estado:
                messages.error(request, "Debes seleccionar un grupo.")
            else:
                try:
                    orden_estado = int(orden_estado)
                except:
                    orden_estado = 0

                grupo = GrupoTrabajo.objects.get(id=id_grupo_estado)

                EstadoTarea.objects.get_or_create(
                    grupo=grupo,
                    nombre=nombre_estado,
                    defaults={
                        "orden": orden_estado,
                        "color": color_estado,
                        "activo": True,
                    }
            )

            messages.success(request, "Estado creado correctamente.")

        elif accion == "toggle_estado":

            id_estado = request.POST.get("id_estado")

            try:

                estado = EstadoTarea.objects.get(id_estado=id_estado)

                estado.activo = not estado.activo
                estado.save()

                if estado.activo:
                    messages.success(request, f"Estado '{estado.nombre}' activado.")
                else:
                    messages.success(request, f"Estado '{estado.nombre}' desactivado.")

            except EstadoTarea.DoesNotExist:
                messages.error(request, "Estado no encontrado.")

        elif accion == "cambiar_color_estado":

            id_estado = request.POST.get("id_estado")
            nuevo_color = request.POST.get("nuevo_color", "#6c757d")

            try:

                estado = EstadoTarea.objects.get(id_estado=id_estado)

                estado.color = nuevo_color
                estado.save()

                messages.success(
                    request,
                    f"Color actualizado para '{estado.nombre}'."
                )

            except EstadoTarea.DoesNotExist:

                messages.error(request, "Estado no encontrado.")

        elif accion == "crear_ambito":

            nombre_ambito = request.POST.get("nombre_ambito", "").strip()

            if not nombre_ambito:
                messages.error(request, "Debes indicar el nombre del ámbito.")
            else:
                AmbitoTarea.objects.get_or_create(
                    nombre=nombre_ambito,
                    defaults={"activo": True},
                )

                messages.success(request, "Ámbito creado correctamente.")

        elif accion == "toggle_ambito":

            id_ambito = request.POST.get("id_ambito")

            try:
                ambito = AmbitoTarea.objects.get(id_ambito=id_ambito)

                ambito.activo = not ambito.activo
                ambito.save()

                if ambito.activo:
                    messages.success(request, f"Ámbito '{ambito.nombre}' activado.")
                else:
                    messages.success(request, f"Ámbito '{ambito.nombre}' desactivado.")

            except AmbitoTarea.DoesNotExist:
                messages.error(request, "Ámbito no encontrado.")

        elif accion == "toggle_admin":

            id_usuario = request.POST.get("id_usuario")

            try:
                perfil = UsuarioGestor.objects.get(pk=id_usuario)

                perfil.es_admin_gestor = not perfil.es_admin_gestor
                perfil.save()

                messages.success(request, "Permiso de administrador actualizado.")

            except UsuarioGestor.DoesNotExist:
                messages.error(request, "Usuario no encontrado.")
                
        elif accion == "crear_tecnico":

            nombre_tecnico = request.POST.get("nombre_tecnico", "").strip()
            id_grupo = request.POST.get("id_grupo_tecnico", "").strip()

            if not nombre_tecnico:
                messages.error(request, "Debes indicar el nombre del técnico.")
            elif not id_grupo:
                messages.error(request, "Debes seleccionar un grupo.")
            else:
                grupo = GrupoTrabajo.objects.get(id=id_grupo)

                tecnico, _ = Tecnico.objects.get_or_create(
                    nombre=nombre_tecnico,
                    defaults={"activo": True},
                )

                TecnicoGrupo.objects.update_or_create(
                    tecnico=tecnico,
                    grupo=grupo,
                    defaults={"activo": True},
                )

                messages.success(request, "Técnico creado/asignado correctamente.")

        elif accion == "toggle_tecnico_grupo":

            id_tecnico = request.POST.get("id_tecnico")
            id_grupo = request.POST.get("id_grupo")

            try:
                relacion = TecnicoGrupo.objects.get(
                    tecnico_id=id_tecnico,
                    grupo_id=id_grupo,
                )

                relacion.activo = not relacion.activo
                relacion.save()

                messages.success(request, "Asignación del técnico actualizada.")

            except TecnicoGrupo.DoesNotExist:
                messages.error(request, "Relación técnico/grupo no encontrada.")

        elif accion == "asignar_usuario_grupo":

            id_usuario = request.POST.get("id_usuario_grupo", "").strip()
            id_grupo = request.POST.get("id_grupo_usuario", "").strip()

            if not id_usuario:
                messages.error(request, "Debes seleccionar un usuario.")
            elif not id_grupo:
                messages.error(request, "Debes seleccionar un grupo.")
            else:
                usuario = User.objects.get(id=id_usuario)
                grupo = GrupoTrabajo.objects.get(id=id_grupo)

                sincronizar_usuario_como_tecnico_en_grupo(
                    user=usuario,
                    grupo=grupo,
                )

                if usuario == request.user:
                    request.session["gestor_tareas_id_grupo"] = grupo.id
                    request.session["gestor_tareas_grupo"] = grupo.nombre

                messages.success(request, "Usuario asignado al grupo correctamente.")

        elif accion == "toggle_usuario_grupo":

            id_relacion = request.POST.get("id_relacion_usuario_grupo", "").strip()

            try:
                relacion = UsuarioGrupo.objects.select_related("usuario", "grupo").get(id=id_relacion)

                relacion.activo = not relacion.activo
                relacion.save()

                if relacion.usuario == request.user and not relacion.activo:
                    request.session.pop("gestor_tareas_id_grupo", None)
                    request.session.pop("gestor_tareas_grupo", None)

                messages.success(request, "Relación usuario/grupo actualizada.")

            except UsuarioGrupo.DoesNotExist:
                messages.error(request, "Relación usuario/grupo no encontrada.")

        return redirect("admin_gestor")

    grupos = GrupoTrabajo.objects.all().order_by("nombre")
    id_grupo_filtro_estados = request.GET.get("grupo_estados", "").strip()

    if not id_grupo_filtro_estados:
        id_grupo_sesion = request.session.get("gestor_tareas_id_grupo")

        if id_grupo_sesion:
            id_grupo_filtro_estados = str(id_grupo_sesion)
        elif grupos.exists():
            id_grupo_filtro_estados = str(grupos.first().id)
            
    usuarios_gestor = (
        UsuarioGestor.objects
        .select_related("user")
        .all()
        .order_by("user__username")
    )
    relaciones = (
        UsuarioGrupo.objects
        .select_related("usuario", "grupo")
        .all()
        .order_by("grupo__nombre", "usuario__username")
    )
    usuarios_auth = User.objects.all().order_by("username")

    estados_gestor = (
        EstadoTarea.objects
        .select_related("grupo")
        .filter(grupo_id=id_grupo_filtro_estados)
        .order_by("grupo__nombre", "orden", "nombre")
    )

    ambitos_gestor = AmbitoTarea.objects.all().order_by("nombre")
    tecnicos_gestor = (
        TecnicoGrupo.objects
        .select_related("tecnico", "grupo")
        .all()
        .order_by("grupo__nombre", "tecnico__nombre")
    )

    context = {
        "grupos": grupos,
        "usuarios_gestor": usuarios_gestor,
        "relaciones": relaciones,
        "estados_gestor": estados_gestor,
        "ambitos_gestor": ambitos_gestor,
        "tecnicos_gestor": tecnicos_gestor,
        "id_grupo_filtro_estados": id_grupo_filtro_estados,
        "usuarios_auth": usuarios_auth,
    }

    return render(request, "gestortareas/admin_gestor.html", context)

