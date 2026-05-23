from pathlib import Path

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from gestor_tareas.models import PerfilUsuario
from gestor_tareas.vistas.common import validar_acceso_gestor

# **************************************************************************
# ************* MI PERFIL DEL GESTOR DE TAREAS ****************
# **************************************************************************
@login_required
def mi_perfil(request):
    acceso = validar_acceso_gestor(request)
    if not acceso:
        messages.error(request, "No tienes permiso o grupo asignado para Gestor de tareas.")
        return redirect("login_gestor_tareas")

    perfil, _ = PerfilUsuario.objects.get_or_create(
        usuario=request.user,
        defaults={
            "nombre_visible": acceso["alias"],
            "email": request.user.email,
        }
    )

    if request.method == "POST":
        perfil.nombre_visible = request.POST.get("nombre_visible", "").strip()
        perfil.puesto = request.POST.get("puesto", "").strip()
        perfil.departamento = request.POST.get("departamento", "").strip()
        perfil.telefono = request.POST.get("telefono", "").strip()
        perfil.email = request.POST.get("email", "").strip()
        perfil.foto_url = request.POST.get("foto_url", "").strip()
        perfil.descripcion = request.POST.get("descripcion", "").strip()

        foto = request.FILES.get("foto")

        if foto:
            extension = Path(foto.name).suffix.lower()

            if extension not in [".jpg", ".jpeg", ".png", ".webp"]:
                messages.error(request, "Formato de imagen no válido. Usa JPG, PNG o WEBP.")
                return redirect("mi_perfil")

            carpeta_perfiles = settings.MEDIA_ROOT / "perfiles"
            carpeta_perfiles.mkdir(parents=True, exist_ok=True)

            nombre_fichero = f"perfil_{request.user.id}{extension}"
            ruta_fichero = carpeta_perfiles / nombre_fichero

            with open(ruta_fichero, "wb+") as destino:
                for chunk in foto.chunks():
                    destino.write(chunk)

            perfil.foto_url = f"{settings.MEDIA_URL}perfiles/{nombre_fichero}"

            perfil.save()

            messages.success(request, "Perfil actualizado correctamente.")
            return redirect("mi_perfil")

    context = {
        "perfil": perfil,
        "grupo_activo_nombre": acceso["grupo"],
    }

    return render(request, "gestortareas/mi_perfil.html", context)