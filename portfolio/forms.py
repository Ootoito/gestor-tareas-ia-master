from django import forms


class ContactoForm(forms.Form):
    nombre = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"autocomplete": "name", "placeholder": "Tu nombre"}))
    correo = forms.EmailField(max_length=254, widget=forms.EmailInput(attrs={"autocomplete": "email", "placeholder": "tu@email.com"}))
    asunto = forms.CharField(max_length=150, widget=forms.TextInput(attrs={"placeholder": "Motivo del contacto"}))
    mensaje = forms.CharField(max_length=4000, widget=forms.Textarea(attrs={"rows": 5, "placeholder": "Escribe tu mensaje..."}))
    web = forms.CharField(required=False, widget=forms.TextInput(attrs={"tabindex": "-1", "autocomplete": "off"}))
