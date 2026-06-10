from django import forms

from praktiko.models import Tema


class TemaForm(forms.ModelForm):
    class Meta:
        model = Tema
        fields = [
            "diccionario",
            "nombre",
            "icono",
            "color",
            "orden",
            "descripcion",
            "activo",
        ]
        widgets = {
            "diccionario": forms.Select(attrs={"class": "form-control"}),
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "icono": forms.TextInput(attrs={"class": "form-control", "placeholder": "👋"}),
            "color": forms.TextInput(attrs={"class": "form-control", "type": "color"}),
            "orden": forms.NumberInput(attrs={"class": "form-control"}),
            "descripcion": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
            "activo": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }

    def __init__(self, *args, **kwargs):
        usuario = kwargs.pop("usuario", None)
        super().__init__(*args, **kwargs)

        if usuario:
            self.fields["diccionario"].queryset = self.fields["diccionario"].queryset.filter(
                usuario=usuario,
                activo=True,
            )