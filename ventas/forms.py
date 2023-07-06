from django import forms
from django.core.validators import EmailValidator, RegexValidator
from .models import Usuario
from datetime import date

class RegistroForm(forms.ModelForm):

    rut = forms.CharField(max_length=12, validators=[
        RegexValidator(
            regex=r'^[\d\.-]{1,3}(\.[\d-]{1,3}){2}-?[\dkK]$',
            message='Ingrese un RUT válido con puntos y/o guiones.'
        )
    ])
    email = forms.CharField(validators=[EmailValidator(message='Ingrese un correo electrónico válido.')])

    fecha_nacimiento = forms.DateField(widget=forms.SelectDateWidget(years=range(1950, date.today().year + 1)))

    class Meta:
        model = Usuario
        fields = ('rut', 'nombre_usuario', 'nombre', 'apellido_paterno', 'apellido_materno', 'email', 'fecha_nacimiento','activo')
