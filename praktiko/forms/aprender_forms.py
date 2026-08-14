from django import forms
from django.utils.translation import gettext_lazy as _

from praktiko.models import Diccionario, Tema


class TemaAprenderChoiceField(forms.ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        return (
            f"{obj.diccionario.icono} {obj.diccionario.nombre} "
            f"— {obj.icono} {obj.nombre}"
        )


class ConfiguracionAprenderForm(forms.Form):
    MODO_ALEATORIO = "aleatorio"
    MODO_ORDEN = "orden"

    MODO_CHOICES = [
        (MODO_ALEATORIO, _("Aleatorio")),
        (MODO_ORDEN, _("Por orden del diccionario")),
    ]

    CANTIDAD_CHOICES = [
        (10, _("10 palabras / frases")),
        (15, _("15 palabras / frases")),
        (20, _("20 palabras / frases")),
        (25, _("25 palabras / frases")),
    ]

    diccionario = forms.ModelChoiceField(
        queryset=Diccionario.objects.none(),
        label=_("Diccionario"),
        widget=forms.Select(attrs={"class": "form-control"}),
    )

    temas = TemaAprenderChoiceField(
        queryset=Tema.objects.none(),
        label=_("Temas"),
        required=False,
        widget=forms.CheckboxSelectMultiple,
        help_text=_(
            "No selecciones ningún tema para utilizar todo el vocabulario "
            "del diccionario."
        ),
    )

    modo_seleccion = forms.ChoiceField(
        label=_("Selección del vocabulario"),
        choices=MODO_CHOICES,
        initial=MODO_ALEATORIO,
        widget=forms.RadioSelect,
    )

    cantidad = forms.TypedChoiceField(
        label=_("Número de elementos"),
        choices=CANTIDAD_CHOICES,
        coerce=int,
        initial=15,
        widget=forms.RadioSelect,
    )

    incluir_ejemplos = forms.BooleanField(
        label=_("Incluir ejemplos"),
        required=False,
        initial=True,
        help_text=_(
            "Si una entrada tiene ejemplos guardados, se mostrarán en la ficha."
        ),
    )

    def __init__(self, *args, **kwargs):
        usuario = kwargs.pop("usuario", None)
        self.usuario = usuario

        super().__init__(*args, **kwargs)

        if usuario:
            # Primera versión: solo diccionarios personales.
            self.fields["diccionario"].queryset = (
                Diccionario.objects
                .filter(
                    usuario=usuario,
                    activo=True,
                    grupo__isnull=True,
                )
                .order_by("nombre")
            )

            self.fields["temas"].queryset = (
                Tema.objects
                .filter(
                    usuario=usuario,
                    activo=True,
                    diccionario__activo=True,
                    diccionario__grupo__isnull=True,
                )
                .select_related("diccionario")
                .order_by(
                    "diccionario__nombre",
                    "orden",
                    "nombre",
                )
            )

    def clean(self):
        cleaned_data = super().clean()

        diccionario = cleaned_data.get("diccionario")
        temas = cleaned_data.get("temas")

        if diccionario and temas:
            temas_invalidos = temas.exclude(diccionario=diccionario)

            if temas_invalidos.exists():
                raise forms.ValidationError(
                    _(
                        "Todos los temas seleccionados deben pertenecer "
                        "al diccionario elegido."
                    )
                )

        return cleaned_data
