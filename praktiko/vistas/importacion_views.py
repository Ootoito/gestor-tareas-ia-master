import csv
import io

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from praktiko.forms.importacion_forms import ImportarVocabularioForm
from praktiko.models import Tema, EntradaDiccionario


@login_required
def importar_vocabulario(request):
    resultado = None

    if request.method == "POST":
        form = ImportarVocabularioForm(request.POST, request.FILES)

        if form.is_valid():
            usuario = form.cleaned_data["usuario"]
            diccionario = form.cleaned_data["diccionario"]
            archivo = form.cleaned_data["archivo_csv"]

            if diccionario.usuario != usuario:
                messages.error(
                    request,
                    "El diccionario seleccionado no pertenece al usuario elegido.",
                )
            else:
                resultado = procesar_csv_vocabulario(
                    usuario=usuario,
                    diccionario=diccionario,
                    archivo=archivo,
                )

                messages.success(
                    request,
                    "Importación procesada correctamente.",
                )
    else:
        form = ImportarVocabularioForm()

    return render(
        request,
        "praktiko/importacion/importar.html",
        {
            "form": form,
            "resultado": resultado,
        },
    )


def procesar_csv_vocabulario(usuario, diccionario, archivo):
    total = 0
    creadas = 0
    duplicadas = 0
    errores = []

    contenido = archivo.read().decode("utf-8-sig")
    reader = csv.DictReader(io.StringIO(contenido), delimiter=";")

    columnas_requeridas = {"tema", "origen", "destino"}

    if not columnas_requeridas.issubset(set(reader.fieldnames or [])):
        return {
            "total": 0,
            "creadas": 0,
            "duplicadas": 0,
            "errores": [
                "El CSV debe contener las columnas: tema;origen;destino"
            ],
        }

    for numero_linea, row in enumerate(reader, start=2):
        total += 1

        try:
            tema_nombre = (row.get("tema") or "").strip()
            texto_origen = (row.get("origen") or "").strip()
            texto_destino = (row.get("destino") or "").strip()

            if not tema_nombre or not texto_origen or not texto_destino:
                errores.append(
                    f"Línea {numero_linea}: tema, origen y destino son obligatorios."
                )
                continue

            tema, _ = Tema.objects.get_or_create(
                usuario=usuario,
                diccionario=diccionario,
                nombre=tema_nombre,
                defaults={
                    "icono": "📁",
                    "color": "#64748b",
                    "activo": True,
                },
            )

            _, creada = EntradaDiccionario.objects.get_or_create(
                usuario=usuario,
                diccionario=diccionario,
                tema=tema,
                texto_origen=texto_origen,
                texto_destino=texto_destino,
                defaults={
                    "tipo": EntradaDiccionario.TIPO_PALABRA,
                    "nivel": EntradaDiccionario.NIVEL_INICIAL,
                    "activa": True,
                },
            )

            if creada:
                creadas += 1
            else:
                duplicadas += 1

        except Exception as exc:
            errores.append(
                f"Línea {numero_linea}: {exc}"
            )

    return {
        "total": total,
        "creadas": creadas,
        "duplicadas": duplicadas,
        "errores": errores,
    }