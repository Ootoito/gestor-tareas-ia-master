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
    Tema,
)
from django.utils import timezone
from praktiko.forms.diccionario_forms import DiccionarioForm
from praktiko.models import Diccionario
from praktiko.forms.tema_forms import TemaForm
from praktiko.forms.tema_forms import TemaGrupoForm
from praktiko.forms.vocabulario_forms import EntradaDiccionarioForm
from praktiko.models import EntradaDiccionario
from praktiko.forms.importacion_forms import ImportarVocabularioForm
from praktiko.vistas.importacion_views import procesar_csv_vocabulario

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

    diccionarios_compartidos = (
        Diccionario.objects
        .filter(
            grupo=grupo,
            activo=True,
        )
        .annotate(
            total_temas=Count("temas", distinct=True),
            total_entradas=Count("entradas", distinct=True),
        )
        .order_by("nombre")
    )
    return render(
        request,
        "praktiko/grupos/detalle.html",
        {
            "grupo": grupo,
            "miembros": miembros,
            "es_admin_grupo": es_admin_grupo,
            "diccionarios_compartidos": diccionarios_compartidos,
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

@login_required
def crear_diccionario_grupo(request, grupo_id):
    grupo = get_object_or_404(
        GrupoAprendizaje,
        id=grupo_id,
        miembros__usuario=request.user,
        miembros__rol=MiembroGrupoAprendizaje.ROL_ADMIN,
        miembros__activo=True,
        activo=True,
    )

    if request.method == "POST":
        form = DiccionarioForm(request.POST)

        if form.is_valid():
            diccionario = form.save(commit=False)
            diccionario.usuario = request.user
            diccionario.grupo = grupo
            diccionario.save()

            messages.success(
                request,
                "Diccionario compartido creado correctamente.",
            )
            return redirect("praktiko:detalle_grupo", grupo_id=grupo.id)
    else:
        form = DiccionarioForm(
            initial={
                "idioma_destino": "Español",
                "icono": "👥",
                "color": "#0f766e",
                "activo": True,
            }
        )

    return render(
        request,
        "praktiko/grupos/formulario_diccionario_grupo.html",
        {
            "form": form,
            "grupo": grupo,
            "titulo": "Nuevo diccionario compartido",
            "boton": "Crear diccionario",
        },
    )

@login_required
def crear_tema_diccionario_grupo(request, grupo_id, diccionario_id):
    grupo = get_object_or_404(
        GrupoAprendizaje,
        id=grupo_id,
        miembros__usuario=request.user,
        miembros__activo=True,
        activo=True,
    )

    diccionario = get_object_or_404(
        Diccionario,
        id=diccionario_id,
        grupo=grupo,
        activo=True,
    )

    if request.method == "POST":
        form = TemaGrupoForm(request.POST)
        print(form.errors)
        if form.is_valid():
            tema = form.save(commit=False)
            tema.usuario = request.user
            tema.diccionario = diccionario
            tema.save()

            messages.success(request, "Tema compartido creado correctamente.")
            return redirect("praktiko:detalle_grupo", grupo_id=grupo.id)
    else:
        form = TemaGrupoForm(
            initial={
                "diccionario": diccionario,
                "icono": "📁",
                "color": "#64748b",
                "activo": True,
            }
        )

    return render(
        request,
        "praktiko/grupos/formulario_tema_grupo.html",
        {
            "form": form,
            "grupo": grupo,
            "diccionario": diccionario,
            "titulo": "Nuevo tema compartido",
            "boton": "Crear tema",
        },
    )

@login_required
def crear_entrada_diccionario_grupo(request, grupo_id, diccionario_id):
    grupo = get_object_or_404(
        GrupoAprendizaje,
        id=grupo_id,
        miembros__usuario=request.user,
        miembros__activo=True,
        activo=True,
    )

    diccionario = get_object_or_404(
        Diccionario,
        id=diccionario_id,
        grupo=grupo,
        activo=True,
    )

    if request.method == "POST":
        form = EntradaDiccionarioForm(request.POST)

        if form.is_valid():
            entrada = form.save(commit=False)
            entrada.usuario = request.user
            entrada.diccionario = diccionario
            entrada.save()

            messages.success(request, "Entrada compartida creada correctamente.")
            return redirect("praktiko:detalle_grupo", grupo_id=grupo.id)
    else:
        form = EntradaDiccionarioForm(
            initial={
                "diccionario": diccionario,
                "tipo": EntradaDiccionario.TIPO_PALABRA,
                "nivel": EntradaDiccionario.NIVEL_INICIAL,
                "activa": True,
            }
        )

    form.fields["diccionario"].queryset = Diccionario.objects.filter(id=diccionario.id)
    form.fields["tema"].queryset = Tema.objects.filter(
        diccionario=diccionario,
        activo=True,
    ).order_by("orden", "nombre")

    return render(
        request,
        "praktiko/grupos/formulario_entrada_grupo.html",
        {
            "form": form,
            "grupo": grupo,
            "diccionario": diccionario,
            "titulo": "Nueva palabra o frase compartida",
            "boton": "Crear entrada",
        },
    )

@login_required
def detalle_diccionario_grupo(request, grupo_id, diccionario_id):
    grupo = get_object_or_404(
        GrupoAprendizaje,
        id=grupo_id,
        miembros__usuario=request.user,
        miembros__activo=True,
        activo=True,
    )

    diccionario = get_object_or_404(
        Diccionario,
        id=diccionario_id,
        grupo=grupo,
        activo=True,
    )

    temas = (
        Tema.objects
        .filter(
            diccionario=diccionario,
            activo=True,
        )
        .annotate(
            total_entradas=Count("entradas", distinct=True),
        )
        .order_by("orden", "nombre")
    )

    entradas = (
        EntradaDiccionario.objects
        .filter(
            diccionario=diccionario,
            activa=True,
        )
        .select_related("tema", "usuario")
        .order_by("tema__orden", "tema__nombre", "texto_origen")
    )

    es_admin_grupo = MiembroGrupoAprendizaje.objects.filter(
        grupo=grupo,
        usuario=request.user,
        rol=MiembroGrupoAprendizaje.ROL_ADMIN,
        activo=True,
    ).exists()

    return render(
        request,
        "praktiko/grupos/detalle_diccionario.html",
        {
            "grupo": grupo,
            "diccionario": diccionario,
            "temas": temas,
            "entradas": entradas,
            "es_admin_grupo": es_admin_grupo,
        },
    )

@login_required
def importar_vocabulario_diccionario_grupo(request, grupo_id, diccionario_id):
    grupo = get_object_or_404(
        GrupoAprendizaje,
        id=grupo_id,
        miembros__usuario=request.user,
        miembros__activo=True,
        activo=True,
    )

    diccionario = get_object_or_404(
        Diccionario,
        id=diccionario_id,
        grupo=grupo,
        activo=True,
    )

    resultado = None

    if request.method == "POST":
        archivo = request.FILES.get("archivo_csv")

        if not archivo:
            messages.error(request, "Debes seleccionar un archivo CSV.")
        else:
            resultado = procesar_csv_vocabulario(
                usuario=request.user,
                diccionario=diccionario,
                archivo=archivo,
            )

            messages.success(request, "Importación procesada correctamente.")

    return render(
        request,
        "praktiko/grupos/importar_diccionario_grupo.html",
        {
            "grupo": grupo,
            "diccionario": diccionario,
            "resultado": resultado,
        },
    )

@login_required
def jugar_diccionario_grupo(request, grupo_id, diccionario_id):
    grupo = get_object_or_404(
        GrupoAprendizaje,
        id=grupo_id,
        miembros__usuario=request.user,
        miembros__activo=True,
        activo=True,
    )

    diccionario = get_object_or_404(
        Diccionario,
        id=diccionario_id,
        grupo=grupo,
        activo=True,
    )

    temas = (
        Tema.objects
        .filter(
            diccionario=diccionario,
            activo=True,
        )
        .order_by("orden", "nombre")
    )

    return render(
        request,
        "praktiko/grupos/jugar_diccionario_grupo.html",
        {
            "grupo": grupo,
            "diccionario": diccionario,
            "temas": temas,
        },
    )

