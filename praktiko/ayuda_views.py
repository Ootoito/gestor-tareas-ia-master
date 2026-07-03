from pathlib import Path

import markdown
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.translation import get_language


@login_required
def manual_usuario(request):
    idioma_actual = (get_language() or "es").split("-")[0]

    idiomas_disponibles = ["es", "en", "ru", "eo"]

    if idioma_actual not in idiomas_disponibles:
        idioma_actual = "es"

    ruta_manual = (
        Path(settings.BASE_DIR)
        / "praktiko"
        / "docs"
        / "manual"
        / f"{idioma_actual}.md"
    )

    if not ruta_manual.exists():
        ruta_manual = (
            Path(settings.BASE_DIR)
            / "praktiko"
            / "docs"
            / "manual"
            / "es.md"
        )

    contenido_md = ruta_manual.read_text(encoding="utf-8")

    contenido_html = markdown.markdown(
        contenido_md,
        extensions=[
            "extra",
            "toc",
            "tables",
            "fenced_code",
        ],
    )

    return render(
        request,
        "praktiko/ayuda/manual.html",
        {
            "contenido_manual": contenido_html,
            "idioma_manual": idioma_actual,
        },
    )