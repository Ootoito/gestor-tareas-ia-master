from django import forms

from praktiko.models import Diccionario


class DiccionarioForm(forms.ModelForm):
    class Meta:
        model = Diccionario
        fields = [
            "nombre",
            "idioma_origen",
            "idioma_destino",
            "icono",
            "color",
            "descripcion",
            "activo",
        ]
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "idioma_origen": forms.TextInput(attrs={"class": "form-control"}),
            "idioma_destino": forms.TextInput(attrs={"class": "form-control"}),
            "icono": forms.TextInput(attrs={"class": "form-control", "placeholder": "🇷🇺"}),
            "color": forms.TextInput(attrs={"class": "form-control", "type": "color"}),
            "descripcion": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
            "activo": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }