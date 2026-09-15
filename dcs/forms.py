from django import forms
from django.utils.text import slugify

from .models import ContenidoDCS, MisionDCS, VersionMisionDCS


class MisionDCSForm(forms.ModelForm):
    class Meta:
        model = MisionDCS

        fields = [
            "numero",
            "titulo",
            "descripcion",
            "url_descarga",
            "activo",
            "orden",
        ]

        labels = {
            "numero": "Número de misión",
            "titulo": "Título",
            "descripcion": "Descripción",
            "url_descarga": "URL de descarga",
            "activo": "Misión activa",
            "orden": "Orden",
        }

        widgets = {
            "numero": forms.NumberInput(
                attrs={
                    "min": 1,
                }
            ),
            "titulo": forms.TextInput(
                attrs={
                    "placeholder": "Título de la misión",
                }
            ),
            "descripcion": forms.Textarea(
                attrs={
                    "rows": 5,
                    "placeholder": "Descripción opcional de la misión",
                }
            ),
            "url_descarga": forms.URLInput(
                attrs={
                    "placeholder": "https://...",
                }
            ),
            "orden": forms.NumberInput(
                attrs={
                    "min": 0,
                }
            ),
        }


    def __init__(self, *args, contenido=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.contenido = contenido

    def clean(self):
        cleaned_data = super().clean()
        numero = cleaned_data.get("numero")

        if numero is None or self.contenido is None:
            return cleaned_data

        existentes = MisionDCS.objects.filter(
            contenido=self.contenido,
            numero=numero,
        )

        if self.instance and self.instance.pk:
            existentes = existentes.exclude(pk=self.instance.pk)

        if existentes.exists():
            self.add_error(
                "numero",
                f"Ya existe la misión número {numero} en este contenido.",
            )

        return cleaned_data


class ContenidoDCSForm(forms.ModelForm):
    """
    Formulario para crear y editar cursos, campañas
    y colecciones de misiones.

    La aeronave no se selecciona desde el formulario:
    se recibe desde la vista de gestión.

    El slug se genera automáticamente a partir del título
    si el usuario lo deja vacío.
    """

    slug = forms.SlugField(
        required=False,
        label="Slug",
        help_text=(
            "Se genera automáticamente a partir del título. "
            "Puedes modificarlo si necesitas una URL concreta."
        ),
        widget=forms.TextInput(
            attrs={
                "placeholder": "Se generará automáticamente",
            }
        ),
    )

    class Meta:
        model = ContenidoDCS

        fields = [
            "titulo",
            "slug",
            "tipo",
            "descripcion",
            "situacion",
            "objetivo",
            "imagen_subida",
            "estado",
            "activo",
            "orden",
        ]

        labels = {
            "titulo": "Título",
            "slug": "Slug",
            "tipo": "Tipo de contenido",
            "descripcion": "Descripción",
            "situacion": "Situación",
            "objetivo": "Objetivo",
            "imagen_subida": "Imagen",
            "estado": "Estado",
            "activo": "Contenido activo",
            "orden": "Orden",
        }

        widgets = {
            "titulo": forms.TextInput(
                attrs={
                    "placeholder": "Título del curso o campaña",
                }
            ),
            "tipo": forms.Select(),
            "descripcion": forms.Textarea(
                attrs={
                    "rows": 5,
                    "placeholder": (
                        "Descripción general del curso, campaña "
                        "o colección de misiones"
                    ),
                }
            ),
            "situacion": forms.Textarea(
                attrs={
                    "rows": 5,
                    "placeholder": (
                        "Situación o contexto de la campaña "
                        "(opcional)"
                    ),
                }
            ),
            "objetivo": forms.Textarea(
                attrs={
                    "rows": 5,
                    "placeholder": (
                        "Objetivo general del curso o campaña "
                        "(opcional)"
                    ),
                }
            ),
            "imagen_subida": forms.ClearableFileInput(
                attrs={
                    "accept": "image/*",
                }
            ),
            "estado": forms.Select(),
            "orden": forms.NumberInput(
                attrs={
                    "min": 0,
                }
            ),
        }

    def __init__(self, *args, aeronave=None, **kwargs):
        super().__init__(*args, **kwargs)

        self.aeronave = aeronave

    def clean_slug(self):
        """
        Si no se introduce slug, se genera automáticamente
        a partir del título.
        """

        slug = self.cleaned_data.get("slug")
        titulo = self.cleaned_data.get("titulo", "")

        if not slug:
            slug = slugify(titulo)

        if not slug:
            raise forms.ValidationError(
                "No se ha podido generar un slug válido."
            )

        return slug

    def clean(self):
        """
        Comprueba que el slug no esté siendo utilizado por otro
        contenido perteneciente a la misma aeronave.
        """

        cleaned_data = super().clean()

        slug = cleaned_data.get("slug")

        if not slug or self.aeronave is None:
            return cleaned_data

        existentes = ContenidoDCS.objects.filter(
            aeronave=self.aeronave,
            slug=slug,
        )

        if self.instance and self.instance.pk:
            existentes = existentes.exclude(
                pk=self.instance.pk,
            )

        if existentes.exists():
            self.add_error(
                "slug",
                (
                    "Ya existe otro contenido con este slug "
                    "para esta aeronave."
                ),
            )

        return cleaned_data

class VersionMisionDCSForm(forms.ModelForm):

    class Meta:
        model = VersionMisionDCS
        fields = ["nombre", "url_descarga", "activo", "orden"]

        labels = {
            "nombre": "Nombre de la versión",
            "url_descarga": "URL de descarga",
            "activo": "Versión activa",
            "orden": "Orden",
        }

        widgets = {
            "nombre": forms.TextInput(
                attrs={
                    "placeholder": "Ej.: Versión estándar, Versión nocturna..."
                }
            ),
            "url_descarga": forms.URLInput(
                attrs={"placeholder": "https://..."}
            ),
            "orden": forms.NumberInput(attrs={"min": 0}),
        }

    def __init__(self, *args, mision=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.mision = mision

    def clean(self):
        cleaned_data = super().clean()
        nombre = cleaned_data.get("nombre")

        if not nombre or self.mision is None:
            return cleaned_data

        existentes = VersionMisionDCS.objects.filter(
            mision=self.mision,
            nombre=nombre,
        )

        if self.instance and self.instance.pk:
            existentes = existentes.exclude(pk=self.instance.pk)

        if existentes.exists():
            self.add_error(
                "nombre",
                "Ya existe una versión con este nombre para esta misión.",
            )

        return cleaned_data
