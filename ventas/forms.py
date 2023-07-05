from django import forms
from .models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = [
            'nombre_usuario',
            'nombre',
            'apellido_paterno',
            'apellido_materno',
            'email',
            'fecha_nacimiento',
		]
