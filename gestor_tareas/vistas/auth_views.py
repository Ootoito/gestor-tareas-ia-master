# =========================================================
# Permisos / acceso
# =========================================================
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

from gestor_tareas.vistas.common import validar_acceso_gestor

def login_gestor_tareas(request):
    """
    Login local del módulo Gestor de tareas.
    Usa usuarios estándar de Django.
    """
    if request.method == "POST":
        username = request.POST.get("usuario", "").strip()
        password = request.POST.get("password", "").strip()

        if not username or not password:
            messages.error(request, "Debes indicar usuario y contraseña.")
            return render(request, "gestortareas/login.html")

        user = authenticate(request, username=username, password=password)

        if user is None:
            messages.error(request, "Usuario o contraseña incorrectos.")
            return render(request, "gestortareas/login.html")

        login(request, user)

        acceso = validar_acceso_gestor(request)
        if not acceso:
            messages.error(request, "Tu usuario no tiene acceso al Gestor de tareas.")
            return render(request, "gestortareas/login.html")

        return redirect("gestor_tareas_home")

    return render(request, "gestortareas/login.html")

def logout_gestor_tareas(request):
    logout(request)
    request.session.flush()
    return redirect("login_gestor_tareas")