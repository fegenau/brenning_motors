from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .forms import LoginForm, Formulario
from .models import Cliente

# Create your views here.

def index(request):
    return render(request, 'index.html')

def productos(request):
    return render(request, 'productos.html')

def modelos(request):
    return render(request, 'modelos.html')

def contacto(request):
    return render(request, 'contacto.html')

def login (request):
    return render(request, 'login.html')

def urbanas (request):
    return render(request, 'urbanas.html')

def vintage (request):
    return render(request, 'vintage.html')

def adventuretouring (request):
    return render(request, 'adventure-touring.html')

def hypernaked (request):
    return render(request, 'hyper-naked.html')

def scooter (request):
    return render(request, 'scooter.html')

def politicas (request):
    return render(request, 'privacy-policy.html')

def atwin(request):
    return render (request, 'africa-twin.html')

def suptenere(request):
    return render (request, 'super-tenere.html')

def tiger(request):
    return render(request, 'tiger.html')

def g310r(request):
    return render(request, 'G310R.html')

def fz25(request):
    return render(request, 'fz25.html')

def xr(request):
    return render(request, 'xr.html')

def formulario (request):
    if request.method == 'POST':
        form = Formulario(request.POST)
        if form.is_valid():
           datos_formulario = form.cleaned_data
           user = User.object.create_user(
                username=datos_formulario.cleaned_data['username'],
                password=datos_formulario.cleaned_data['password']
           )
           mi_objeto = Cliente (
                rut=datos_formulario['rut'],
                id_usuario=datos_formulario['id_usuario'],
                nombre=datos_formulario['nombre'],
                apellido=datos_formulario['apellido'],
                sexo=datos_formulario['sexo'],
                fechanacimiento=datos_formulario['fechanacimiento'],
                direccion=datos_formulario['direccion'],
                telefono=datos_formulario['telefono'],
                email=datos_formulario['email']
                
            )
           mi_objeto.save()
        return redirect('formulario')
    else:
        form = Formulario()
    
    return render(request, 'formulario.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('formulario')  # Redirige a la página después de iniciar sesión
            else:
                form.add_error(None, 'Nombre de usuario o contraseña incorrectos.')
    else:
        form = LoginForm()
    
    return render(request, 'login.html', {'form': form})



