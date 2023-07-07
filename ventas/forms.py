from django import forms
from django.core.validators import RegexValidator
from .models import Usuario
from django.utils import timezone
from django.contrib.auth.forms import AuthenticationForm


class RegistroUsuarioForm(forms.ModelForm):
    rut = forms.CharField(max_length=12, validators=[
        RegexValidator(r'^\d{1,2}(\.\d{3}){2}-[\dkK]$','Ingrese un RUT válido.'
                       )])
    email = forms.EmailField()
    fecha_nacimiento = forms.DateField(widget=forms.SelectDateWidget(years=range(1950, timezone.now().year + 1)))
    contraseña = forms.CharField(widget=forms.PasswordInput)
    confirmar_contraseña = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ['rut', 'nombre_usuario', 'contraseña', 'confirmar_contraseña', 'nombre', 'apellido_paterno', 'apellido_materno', 'email', 'fecha_nacimiento']

    def clean(self):
        cleaned_data = super().clean()
        contraseña = cleaned_data.get("contraseña")
        confirmar_contraseña = cleaned_data.get("confirmar_contraseña")

        if contraseña and confirmar_contraseña and contraseña != confirmar_contraseña:
            self.add_error('confirmar_contraseña', "Las contraseñas no coinciden.")

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Nombre de usuario'
        self.fields['password'].label = 'Contraseña'