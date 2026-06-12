from django import forms
from django.contrib.auth.models import User

from praktiko.models import Diccionario


class ImportarVocabularioForm(forms.Form):
    usuario = forms.ModelChoiceField(
        queryset=User.objects.none(),
        label="Usuario",
        widget=forms.Select(attrs={"class": "form-control"}),
    )

    diccionario = forms.ModelChoiceField(
        queryset=Diccionario.objects.none(),
        label="Diccionario",
        widget=forms.Select(attrs={"class": "form-control"}),
    )

    archivo_csv = forms.FileField(
        label="Archivo CSV",
        widget=forms.ClearableFileInput(attrs={"class": "form-control"}),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["usuario"].queryset = User.objects.filter(
            groups__name="Praktiko",
            is_active=True,
        ).order_by("username")

        self.fields["diccionario"].queryset = Diccionario.objects.filter(
            activo=True,
        ).select_related("usuario").order_by(
            "usuario__username",
            "nombre",
        )