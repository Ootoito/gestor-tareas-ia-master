from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render

from praktiko.forms.grupo_forms import GrupoAprendizajeForm
from praktiko.models import GrupoAprendizaje, MiembroGrupoAprendizaje
from django.contrib.auth.models import User
from praktiko.forms.grupo_forms import GrupoAprendizajeForm, InvitarUsuarioGrupoForm
from praktiko.models import (
    GrupoAprendizaje,
    MiembroGrupoAprendizaje,
    InvitacionGrupoAprendizaje,
)
from django.utils import timezone

@login_required
def listado_grupos(request):
    grupos = (
        GrupoAprendizaje.objects
        .filter(
            miembros__usuario=request.user,
            miembros__activo=True,
            activo=True,
        )
        .annotate(total_miembros=Count("miembros", distinct=True))
        .order_by("nombre")
    )

    return render(
        request,
        "praktiko/grupos/listado.html",
        {
            "grupos": grupos,
        },
    )


@login_required
def crear_grupo(request):
    if request.method == "POST":
        form = GrupoAprendizajeForm(request.POST)

        if form.is_valid():
            grupo = form.save(commit=False)
            grupo.creador = request.user
            grupo.save()

            MiembroGrupoAprendizaje.objects.create(
                grupo=grupo,
                usuario=request.user,
                rol=MiembroGrupoAprendizaje.ROL_ADMIN,
                activo=True,
            )

            messages.success(request, "Grupo creado correctamente.")
            return redirect("praktiko:listado_grupos")
    else:
        form = GrupoAprendizajeForm(
            initial={
                "activo": True,
            }
        )

    return render(
        request,
        "praktiko/grupos/formulario.html",
        {
            "form": form,
            "titulo": "Nuevo grupo",
            "boton": "Crear grupo",
        },
    )

@login_required
def detalle_grupo(request, grupo_id):
    grupo = get_object_or_404(
        GrupoAprendizaje,
        id=grupo_id,
        miembros__usuario=request.user,
        miembros__activo=True,
        activo=True,
    )

    miembros = (
        MiembroGrupoAprendizaje.objects
        .filter(grupo=grupo, activo=True)
        .select_related("usuario")
        .order_by("rol", "usuario__username")
    )

    es_admin_grupo = MiembroGrupoAprendizaje.objects.filter(
        grupo=grupo,
        usuario=request.user,
        rol=MiembroGrupoAprendizaje.ROL_ADMIN,
        activo=True,
    ).exists()

    return render(
        request,
        "praktiko/grupos/detalle.html",
        {
            "grupo": grupo,
            "miembros": miembros,
            "es_admin_grupo": es_admin_grupo,
        },
    )

@login_required
def invitar_usuario_grupo(request, grupo_id):
    grupo = get_object_or_404(
        GrupoAprendizaje,
        id=grupo_id,
        miembros__usuario=request.user,
        miembros__rol=MiembroGrupoAprendizaje.ROL_ADMIN,
        miembros__activo=True,
        activo=True,
    )

    if request.method == "POST":
        form = InvitarUsuarioGrupoForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data["email"].strip().lower()

            try:
                invitado = User.objects.get(
                    email__iexact=email,
                    groups__name="Praktiko",
                    is_active=True,
                )
            except User.DoesNotExist:
                messages.error(
                    request,
                    "No existe ningún usuario Praktiko activo con ese email.",
                )
                return redirect("praktiko:invitar_usuario_grupo", grupo_id=grupo.id)

            if MiembroGrupoAprendizaje.objects.filter(
                grupo=grupo,
                usuario=invitado,
                activo=True,
            ).exists():
                messages.error(request, "Ese usuario ya pertenece al grupo.")
                return redirect("praktiko:detalle_grupo", grupo_id=grupo.id)

            if InvitacionGrupoAprendizaje.objects.filter(
                grupo=grupo,
                invitado=invitado,
                estado=InvitacionGrupoAprendizaje.ESTADO_PENDIENTE,
            ).exists():
                messages.error(request, "Ese usuario ya tiene una invitación pendiente.")
                return redirect("praktiko:detalle_grupo", grupo_id=grupo.id)

            InvitacionGrupoAprendizaje.objects.create(
                grupo=grupo,
                invitado=invitado,
                invitado_por=request.user,
                email=email,
                estado=InvitacionGrupoAprendizaje.ESTADO_PENDIENTE,
            )

            messages.success(request, "Invitación enviada correctamente.")
            return redirect("praktiko:detalle_grupo", grupo_id=grupo.id)
    else:
        form = InvitarUsuarioGrupoForm()

    return render(
        request,
        "praktiko/grupos/invitar.html",
        {
            "form": form,
            "grupo": grupo,
        },
    )

@login_required
def mis_invitaciones(request):
    invitaciones = (
        InvitacionGrupoAprendizaje.objects
        .filter(
            invitado=request.user,
            estado=InvitacionGrupoAprendizaje.ESTADO_PENDIENTE,
        )
        .select_related("grupo", "invitado_por")
        .order_by("-creada_en")
    )

    return render(
        request,
        "praktiko/grupos/invitaciones.html",
        {
            "invitaciones": invitaciones,
        },
    )

@login_required
def aceptar_invitacion(request, invitacion_id):
    invitacion = get_object_or_404(
        InvitacionGrupoAprendizaje,
        id=invitacion_id,
        invitado=request.user,
        estado=InvitacionGrupoAprendizaje.ESTADO_PENDIENTE,
    )

    MiembroGrupoAprendizaje.objects.get_or_create(
        grupo=invitacion.grupo,
        usuario=request.user,
        defaults={
            "rol": MiembroGrupoAprendizaje.ROL_MIEMBRO,
            "activo": True,
        }
    )

    invitacion.estado = InvitacionGrupoAprendizaje.ESTADO_ACEPTADA
    invitacion.respondida_en = timezone.now()
    invitacion.save()

    messages.success(
        request,
        f"Te has unido al grupo '{invitacion.grupo.nombre}'."
    )

    return redirect("praktiko:listado_grupos")

@login_required
def rechazar_invitacion(request, invitacion_id):
    invitacion = get_object_or_404(
        InvitacionGrupoAprendizaje,
        id=invitacion_id,
        invitado=request.user,
        estado=InvitacionGrupoAprendizaje.ESTADO_PENDIENTE,
    )

    invitacion.estado = InvitacionGrupoAprendizaje.ESTADO_RECHAZADA
    invitacion.respondida_en = timezone.now()
    invitacion.save()

    messages.info(
        request,
        f"Has rechazado la invitación al grupo '{invitacion.grupo.nombre}'."
    )

    return redirect("praktiko:mis_invitaciones")

@login_required
def salir_grupo(request, grupo_id):
    grupo = get_object_or_404(
        GrupoAprendizaje,
        id=grupo_id,
        miembros__usuario=request.user,
        miembros__activo=True,
        activo=True,
    )

    miembro = get_object_or_404(
        MiembroGrupoAprendizaje,
        grupo=grupo,
        usuario=request.user,
        activo=True,
    )

    if miembro.rol == MiembroGrupoAprendizaje.ROL_ADMIN:
        total_admins = MiembroGrupoAprendizaje.objects.filter(
            grupo=grupo,
            rol=MiembroGrupoAprendizaje.ROL_ADMIN,
            activo=True,
        ).count()

        if total_admins <= 1:
            messages.error(
                request,
                "No puedes salir del grupo porque eres el único administrador.",
            )
            return redirect("praktiko:detalle_grupo", grupo_id=grupo.id)

    miembro.activo = False
    miembro.save(update_fields=["activo"])

    messages.success(request, f"Has salido del grupo '{grupo.nombre}'.")

    return redirect("praktiko:listado_grupos")