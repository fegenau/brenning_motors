from django import forms
from django.core.validators import EmailValidator, RegexValidator
from .models import Usuario
from datetime import date
from django.contrib.auth.forms import AuthenticationForm



class RegistroForm(forms.ModelForm):
    rut = forms.CharField(max_length=12, validators=[RegexValidator(r'^\d{1,3}(\.\d{1,3}){2}-[\dkK]$','Ingrese un RUT válido.')])
    email = forms.EmailField()
    fecha_nacimiento = forms.DateField(widget=forms.SelectDateWidget(years=range(1960, date.today().year + 1)))

    class Meta:
        model = Usuario
        fields = ('rut', 'nombre_usuario', 'contraseña', 'nombre', 'apellido_paterno', 'apellido_materno', 'email', 'fecha_nacimiento', 'activo')

    def clean_rut(self):
        rut = self.cleaned_data['rut']
        rut = rut.replace('.', '').replace('-', '')  # Remover puntos y guion
        rut_con_formato = '-'.join([rut[:-1], rut[-1]])  # Agregar guion antes del dígito verificador

        # Verificar si el RUT ya existe en la base de datos
        if Usuario.objects.filter(rut=rut_con_formato).exists():
            raise forms.ValidationError('El RUT ingresado ya está registrado.')

        return rut_con_formato



class LoginForm(AuthenticationForm):
    def confirm_login_allowed(self, user):
        if not user.activo:
            raise forms.ValidationError('Tu cuenta está desactivada.')
