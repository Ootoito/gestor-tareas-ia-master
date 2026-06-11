from django import forms
from django.contrib.auth.models import User


class UsuarioPraktikoForm(forms.ModelForm):
    password_inicial = forms.CharField(
        label="Contraseña inicial",
        required=False,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Solo necesaria al crear usuario",
            }
        ),
    )

    es_admin_praktiko = forms.BooleanField(
        label="Administrador Praktiko",
        required=False,
        widget=forms.CheckboxInput(attrs={"class": "form-check-input"}),
    )

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
            "is_active",
        ]
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "is_active": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }

    def __init__(self, *args, **kwargs):
        self.es_creacion = kwargs.pop("es_creacion", False)
        super().__init__(*args, **kwargs)

        if self.instance and self.instance.pk:
            self.fields["es_admin_praktiko"].initial = self.instance.groups.filter(
                name="PraktikoAdmin"
            ).exists()

        if self.es_creacion:
            self.fields["password_inicial"].required = True

    def clean_username(self):
        username = self.cleaned_data["username"]

        qs = User.objects.filter(username=username)

        if self.instance and self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)

        if qs.exists():
            raise forms.ValidationError("Ya existe un usuario con ese nombre.")

        return username