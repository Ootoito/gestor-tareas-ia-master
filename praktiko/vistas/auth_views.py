from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

from praktiko.forms.login_forms import PraktikoLoginForm


def login_praktiko(request):
    if request.user.is_authenticated:
        return redirect("praktiko:home")

    if request.method == "POST":
        form = PraktikoLoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(
                request,
                username=username,
                password=password,
            )

            if user is not None:
                login(request, user)
                messages.success(request, "Sesión iniciada correctamente.")
                return redirect("praktiko:home")

            messages.error(request, "Usuario o contraseña incorrectos.")
    else:
        form = PraktikoLoginForm()

    return render(
        request,
        "praktiko/auth/login.html",
        {
            "form": form,
        },
    )


def logout_praktiko(request):
    logout(request)
    messages.success(request, "Sesión cerrada correctamente.")
    return redirect("praktiko:login")