from django import forms
from django.utils.translation import gettext_lazy as _

from praktiko.models import Diccionario, Examen, Tema


class TemaExamenChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return (
            f"{obj.diccionario.icono} {obj.diccionario.nombre} "
            f"- {obj.icono} {obj.nombre}"
        )


class ConfiguracionExamenForm(forms.Form):
    NUMERO_PREGUNTAS_CHOICES = [
        (15, _("15 preguntas")),
        (25, _("25 preguntas")),
    ]

    diccionario = forms.ModelChoiceField(
        queryset=Diccionario.objects.none(),
        label=_("Diccionario"),
        widget=forms.Select(attrs={"class": "form-control"}),
    )

    tema = TemaExamenChoiceField(
        queryset=Tema.objects.none(),
        label=_("Tema"),
        required=False,
        empty_label=_("Todos los temas"),
        widget=forms.Select(attrs={"class": "form-control"}),
    )

    numero_preguntas = forms.TypedChoiceField(
        label=_("Número de preguntas"),
        choices=NUMERO_PREGUNTAS_CHOICES,
        coerce=int,
        initial=15,
        widget=forms.RadioSelect,
    )

    sentido = forms.ChoiceField(
        label=_("Sentido"),
        choices=Examen.SENTIDO_CHOICES,
        initial=Examen.SENTIDO_MIXTO,
        widget=forms.RadioSelect,
    )

    def __init__(self, *args, **kwargs):
        usuario = kwargs.pop("usuario", None)
        self.usuario = usuario
        super().__init__(*args, **kwargs)

        if usuario:
            self.fields["diccionario"].queryset = (
                Diccionario.objects.filter(
                    usuario=usuario,
                    activo=True,
                )
                .order_by("nombre")
            )

            self.fields["tema"].queryset = (
                Tema.objects.filter(
                    usuario=usuario,
                    activo=True,
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
        tema = cleaned_data.get("tema")

        if diccionario and tema and tema.diccionario_id != diccionario.id:
            raise forms.ValidationError(
                _("El tema seleccionado no pertenece al diccionario elegido.")
            )

        return cleaned_data
