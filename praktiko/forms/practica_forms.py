from django import forms

from praktiko.models import Diccionario, SesionPractica, Tema


class TemaChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return f"{obj.diccionario.icono} {obj.diccionario.nombre} - {obj.icono} {obj.nombre}"


class ConfiguracionPracticaForm(forms.Form):
    diccionario = forms.ModelChoiceField(
        queryset=Diccionario.objects.none(),
        label="Diccionario",
        widget=forms.Select(attrs={"class": "form-control"}),
    )

    tema = TemaChoiceField(
        queryset=Tema.objects.none(),
        label="Tema",
        required=False,
        widget=forms.Select(attrs={"class": "form-control"}),
    )

    numero_preguntas = forms.IntegerField(
        label="Número de preguntas",
        min_value=1,
        max_value=50,
        initial=10,
        widget=forms.NumberInput(attrs={"class": "form-control"}),
    )

    modo = forms.ChoiceField(
        label="Modo",
        choices=SesionPractica.MODO_CHOICES,
        initial=SesionPractica.MODO_TEMA,
        widget=forms.Select(attrs={"class": "form-control"}),
    )

    def __init__(self, *args, **kwargs):
        usuario = kwargs.pop("usuario", None)
        self.usuario = usuario

        super().__init__(*args, **kwargs)

        if usuario:
            self.fields["diccionario"].queryset = Diccionario.objects.filter(
                usuario=usuario,
                activo=True,
            ).order_by("nombre")

            self.fields["tema"].queryset = Tema.objects.filter(
                usuario=usuario,
                activo=True,
            ).select_related("diccionario").order_by(
                "diccionario__nombre",
                "orden",
                "nombre",
            )

    def clean(self):
        cleaned_data = super().clean()

        diccionario = cleaned_data.get("diccionario")
        tema = cleaned_data.get("tema")

        if diccionario and tema:
            if tema.diccionario_id != diccionario.id:
                raise forms.ValidationError(
                    "El tema seleccionado no pertenece al diccionario elegido."
                )

        return cleaned_data