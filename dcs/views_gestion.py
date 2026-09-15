from functools import wraps

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ContenidoDCSForm, MisionDCSForm
from .models import Aeronave, ContenidoDCS, MisionDCS


# ============================================================
# PERMISOS DE GESTIÓN DCS
# ============================================================

def usuario_dcs_admin(user):
    return (
        user.is_authenticated
        and (
            user.is_superuser
            or user.groups.filter(name="DCSAdmin").exists()
        )
    )


def dcs_admin_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("dcs:gestion_login")

        if not usuario_dcs_admin(request.user):
            return render(
                request,
                "dcs/gestion/sin_permisos.html",
                status=403,
            )

        return view_func(request, *args, **kwargs)

    return wrapper


# ============================================================
# LOGIN / LOGOUT
# ============================================================

def gestion_login(request):
    if usuario_dcs_admin(request.user):
        return redirect("dcs:gestion")

    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "")

        user = authenticate(
            request,
            username=username,
            password=password,
        )

        if user is None:
            messages.error(
                request,
                "Usuario o contraseña incorrectos.",
            )

        elif not usuario_dcs_admin(user):
            messages.error(
                request,
                "Este usuario no tiene acceso a la gestión DCS.",
            )

        else:
            login(request, user)
            return redirect("dcs:gestion")

    return render(
        request,
        "dcs/gestion/login.html",
    )


@dcs_admin_required
def gestion_logout(request):
    logout(request)
    return redirect("dcs:gestion_login")


# ============================================================
# PANEL PRINCIPAL
# ============================================================

@dcs_admin_required
def gestion_panel(request):
    aeronaves = (
        Aeronave.objects
        .prefetch_related("contenidos__misiones")
        .order_by("orden", "nombre")
    )

    contexto = {
        "aeronaves": aeronaves,
        "total_aeronaves": Aeronave.objects.count(),
        "total_contenidos": ContenidoDCS.objects.count(),
        "total_misiones": MisionDCS.objects.count(),
    }

    return render(
        request,
        "dcs/gestion/panel.html",
        contexto,
    )


# ============================================================
# GESTIÓN DE UNA AERONAVE
# ============================================================

@dcs_admin_required
def gestion_aeronave(request, aeronave_id):
    aeronave = get_object_or_404(
        Aeronave.objects.prefetch_related("contenidos__misiones"),
        pk=aeronave_id,
    )

    contenidos = (
        aeronave.contenidos
        .all()
        .order_by("orden", "titulo")
    )

    return render(
        request,
        "dcs/gestion/aeronave.html",
        {
            "aeronave": aeronave,
            "contenidos": contenidos,
        },
    )


# ============================================================
# CREAR CONTENIDO
# ============================================================

@dcs_admin_required
def gestion_contenido_nuevo(request, aeronave_id):
    aeronave = get_object_or_404(
        Aeronave,
        pk=aeronave_id,
    )

    if request.method == "POST":
        form = ContenidoDCSForm(
            request.POST,
            request.FILES,
            aeronave=aeronave,
        )

        if form.is_valid():
            contenido = form.save(commit=False)
            contenido.aeronave = aeronave
            contenido.save()

            messages.success(
                request,
                f'Contenido "{contenido.titulo}" creado correctamente.',
            )

            return redirect(
                "dcs:gestion_aeronave",
                aeronave_id=aeronave.id,
            )

    else:
        ultimo_orden = (
            aeronave.contenidos
            .order_by("-orden")
            .values_list("orden", flat=True)
            .first()
        )

        form = ContenidoDCSForm(
            aeronave=aeronave,
            initial={
                "estado": ContenidoDCS.ESTADO_DESARROLLO,
                "activo": True,
                "orden": (ultimo_orden or 0) + 10,
            },
        )

    return render(
        request,
        "dcs/gestion/contenido_form.html",
        {
            "form": form,
            "contenido": None,
            "aeronave": aeronave,
            "es_nuevo": True,
        },
    )


# ============================================================
# EDITAR CONTENIDO
# ============================================================

@dcs_admin_required
def gestion_contenido_editar(request, contenido_id):
    contenido = get_object_or_404(
        ContenidoDCS.objects.select_related("aeronave"),
        pk=contenido_id,
    )

    aeronave = contenido.aeronave

    if request.method == "POST":
        form = ContenidoDCSForm(
            request.POST,
            request.FILES,
            instance=contenido,
            aeronave=aeronave,
        )

        if form.is_valid():
            contenido = form.save()

            messages.success(
                request,
                f'Contenido "{contenido.titulo}" actualizado correctamente.',
            )

            return redirect(
                "dcs:gestion_aeronave",
                aeronave_id=aeronave.id,
            )

    else:
        form = ContenidoDCSForm(
            instance=contenido,
            aeronave=aeronave,
        )

    return render(
        request,
        "dcs/gestion/contenido_form.html",
        {
            "form": form,
            "contenido": contenido,
            "aeronave": aeronave,
            "es_nuevo": False,
        },
    )


# ============================================================
# ELIMINAR CONTENIDO
# ============================================================

@dcs_admin_required
def gestion_contenido_eliminar(request, contenido_id):
    contenido = get_object_or_404(
        ContenidoDCS.objects.select_related("aeronave"),
        pk=contenido_id,
    )

    aeronave = contenido.aeronave
    numero_misiones = contenido.misiones.count()
    puede_eliminar = numero_misiones == 0

    if request.method == "POST":
        if not puede_eliminar:
            messages.error(
                request,
                (
                    f'No se puede eliminar "{contenido.titulo}" '
                    f'porque contiene {numero_misiones} '
                    f'{"misión" if numero_misiones == 1 else "misiones"}.'
                ),
            )

            return redirect(
                "dcs:gestion_aeronave",
                aeronave_id=aeronave.id,
            )

        titulo = contenido.titulo
        contenido.delete()

        messages.success(
            request,
            f'Contenido "{titulo}" eliminado correctamente.',
        )

        return redirect(
            "dcs:gestion_aeronave",
            aeronave_id=aeronave.id,
        )

    return render(
        request,
        "dcs/gestion/contenido_confirmar_eliminar.html",
        {
            "contenido": contenido,
            "aeronave": aeronave,
            "numero_misiones": numero_misiones,
            "puede_eliminar": puede_eliminar,
        },
    )


# ============================================================
# LISTADO DE MISIONES
# ============================================================

@dcs_admin_required
def gestion_misiones(request, contenido_id):
    contenido = get_object_or_404(
        ContenidoDCS.objects.select_related("aeronave"),
        pk=contenido_id,
    )

    misiones = (
        contenido.misiones
        .all()
        .order_by("orden", "numero")
    )

    return render(
        request,
        "dcs/gestion/misiones.html",
        {
            "aeronave": contenido.aeronave,
            "contenido": contenido,
            "misiones": misiones,
        },
    )


# ============================================================
# EDITAR MISIÓN
# ============================================================

@dcs_admin_required
def gestion_mision_editar(request, mision_id):
    mision = get_object_or_404(
        MisionDCS.objects.select_related(
            "contenido",
            "contenido__aeronave",
        ),
        pk=mision_id,
    )

    if request.method == "POST":
        form = MisionDCSForm(
            request.POST,
            instance=mision,
        )

        if form.is_valid():
            form.save()

            messages.success(
                request,
                f'Misión "{mision.titulo}" actualizada correctamente.',
            )

            return redirect(
                "dcs:gestion_misiones",
                contenido_id=mision.contenido.id,
            )

    else:
        form = MisionDCSForm(instance=mision)

    return render(
        request,
        "dcs/gestion/mision_form.html",
        {
            "form": form,
            "mision": mision,
            "contenido": mision.contenido,
            "aeronave": mision.contenido.aeronave,
            "es_nueva": False,
        },
    )


# ============================================================
# CREAR MISIÓN
# ============================================================

@dcs_admin_required
def gestion_mision_nueva(request, contenido_id):
    contenido = get_object_or_404(
        ContenidoDCS.objects.select_related("aeronave"),
        pk=contenido_id,
    )

    if request.method == "POST":
        form = MisionDCSForm(request.POST)

        if form.is_valid():
            mision = form.save(commit=False)
            mision.contenido = contenido
            mision.save()

            messages.success(
                request,
                f'Misión "{mision.titulo}" creada correctamente.',
            )

            return redirect(
                "dcs:gestion_misiones",
                contenido_id=contenido.id,
            )

    else:
        ultimo_numero = (
            contenido.misiones
            .order_by("-numero")
            .values_list("numero", flat=True)
            .first()
        )

        ultimo_orden = (
            contenido.misiones
            .order_by("-orden")
            .values_list("orden", flat=True)
            .first()
        )

        form = MisionDCSForm(
            initial={
                "numero": (ultimo_numero or 0) + 1,
                "orden": (ultimo_orden or 0) + 1,
                "activo": True,
            }
        )

    return render(
        request,
        "dcs/gestion/mision_form.html",
        {
            "form": form,
            "mision": None,
            "contenido": contenido,
            "aeronave": contenido.aeronave,
            "es_nueva": True,
        },
    )


# ============================================================
# ELIMINAR MISIÓN
# ============================================================

@dcs_admin_required
def gestion_mision_eliminar(request, mision_id):
    mision = get_object_or_404(
        MisionDCS.objects.select_related(
            "contenido",
            "contenido__aeronave",
        ),
        pk=mision_id,
    )

    contenido = mision.contenido
    aeronave = contenido.aeronave

    if request.method == "POST":
        titulo = mision.titulo
        numero = mision.numero

        mision.delete()

        messages.success(
            request,
            f'Misión {numero:02d} "{titulo}" eliminada correctamente.',
        )

        return redirect(
            "dcs:gestion_misiones",
            contenido_id=contenido.id,
        )

    return render(
        request,
        "dcs/gestion/mision_confirmar_eliminar.html",
        {
            "mision": mision,
            "contenido": contenido,
            "aeronave": aeronave,
        },
    )