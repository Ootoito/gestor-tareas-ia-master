from django import forms

from praktiko.models import GrupoAprendizaje


class GrupoAprendizajeForm(forms.ModelForm):
    class Meta:
        model = GrupoAprendizaje
        fields = [
            "nombre",
            "descripcion",
            "activo",
        ]
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "descripcion": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
            "activo": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }

class InvitarUsuarioGrupoForm(forms.Form):
    email = forms.EmailField(
        label="Email del usuario",
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "usuario@email.com",
            }
        ),
    )