from django import forms
from django.core.validators import RegexValidator
from .models import Usuario

class RegistroUsuarioForm(forms.ModelForm):
    
    class Meta:
        model = Usuario
        fields = ['rut', 'nombre', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }

class LoginForm(forms.Form):
    rut = forms.CharField(label='RUT', max_length=12)
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)