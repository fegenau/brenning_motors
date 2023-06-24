from django import forms
from .models import Usuario

class RegistroForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ('rut', 'tipo_usuario', 'password')

class LoginForm(forms.Form):
    rut = forms.IntegerField()
    password = forms.CharField(widget=forms.PasswordInput)