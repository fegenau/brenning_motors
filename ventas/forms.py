from django import forms
from django.contrib.auth.models import User

class Formulario(forms.Form):
    rut = forms.CharField(max_length=12)
    id_usuario = forms.CharField(max_length=20)
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    sexo = forms.ChoiceField(choices=[('M', 'Masculino'), ('F', 'Femenino')])
    fechanacimiento = forms.DateField()
    direccion = forms.CharField(max_length=200)
    telefono = forms.CharField(max_length=15)
    email = forms.EmailField()
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput())

    class LoginForm(forms.Form):
        username = forms.CharField(max_length=100)
        password = forms.CharField(widget=forms.PasswordInput)