from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import RegistroForm, LoginForm
from django.contrib.auth import login
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

def vintage (request):
    return render(request, 'vintage.html')

def caferacer (request):
    return render(request, 'caferacer.html')

def ducati1100 (request):
    return render(request, 'ducati1100.html')

def z650 (request):
    return render(request, 'z650.html')

def urbanas (request):
    return render(request, 'urbanas.html')

def vintage (request):
    return render(request, 'vintage.html')

def adventuretouring (request):
    return render(request, 'adventure-touring.html')

def politicas (request):
    return render(request, 'privacy-policy.html')

def atwin(request):
    return render (request, 'africa-twin.html')

def suptenere(request):
    return render (request, 'super-tenere.html')

def tiger(request):
    return render(request, 'tiger.html')

#scooters
def scooters (request):
    return render(request, 'Scooters/scooters.html')

def VespaPrimavera(request):
    return render(request, 'Scooters/VespaPrimavera.html')

def HondaPCX(request):
    return render(request, 'Scooters/HondaPCX.html')

def YamahaNMAX(request):
    return render(request, 'Scooters/YamahaNMAX.html')

def hyperNaked (request):
    return render(request, 'hyperNaked.html')

def cb190 (request):
    return render(request, 'cb190.html')

def mT07 (request):
    return render(request, 'mT07.html')

def streetTripleRS (request):
    return render(request, 'streetTripleRS.html')

def g310r(request):
    return render(request, 'G310R.html')

def fz25(request):
    return render(request, 'fz25.html')

def xr(request):
    return render(request, 'xr.html')

def cb190(request):
    return render(request, 'cb190.html')

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro exitoso.')
            return redirect('registro/')
    else:
        form = RegistroForm()
    return render(request, 'registro.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # Acción adicional después de un inicio de sesión exitoso
            # Por ejemplo, redireccionar a una página de perfil
            return redirect('perfil')
    else:
        form = LoginForm(request)
    return render(request, 'login.html', {'form': form})