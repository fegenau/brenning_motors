from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Usuario
from .forms import RegistroForm,LoginForm


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

def cb190(request):
    return render(request, 'cb190.html')

def registro_cliente(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = RegistroForm()
    return render(request, 'registro.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            rut = form.cleaned_data['rut']
            password = form.cleaned_data['password']
            try:
                usuario = Usuario.objects.get(rut=rut, password=password)
                # Realizar acciones adicionales después de iniciar sesión
                return redirect('/')
            except Usuario.DoesNotExist:
                form.add_error(None, 'Credenciales inválidas')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})






