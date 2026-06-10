from django import forms

from praktiko.models import EntradaDiccionario, Tema


class EntradaDiccionarioForm(forms.ModelForm):
    class Meta:
        model = EntradaDiccionario
        fields = [
            "diccionario",
            "tema",
            "tipo",
            "texto_origen",
            "texto_destino",
            "ejemplo_origen",
            "ejemplo_destino",
            "notas",
            "nivel",
            "activa",
        ]
        widgets = {
            "diccionario": forms.Select(attrs={"class": "form-control"}),
            "tema": forms.Select(attrs={"class": "form-control"}),
            "tipo": forms.Select(attrs={"class": "form-control"}),
            "texto_origen": forms.TextInput(attrs={"class": "form-control"}),
            "texto_destino": forms.TextInput(attrs={"class": "form-control"}),
            "ejemplo_origen": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
            "ejemplo_destino": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
            "notas": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
            "nivel": forms.Select(attrs={"class": "form-control"}),
            "activa": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }

    def __init__(self, *args, **kwargs):
        usuario = kwargs.pop("usuario", None)
        super().__init__(*args, **kwargs)

        if usuario:
            self.fields["diccionario"].queryset = self.fields["diccionario"].queryset.filter(
                usuario=usuario,
                activo=True,
            )

            self.fields["tema"].queryset = Tema.objects.filter(
                usuario=usuario,
                activo=True,
            ).select_related("diccionario").order_by(
                "diccionario__nombre",
                "orden",
                "nombre",
            )