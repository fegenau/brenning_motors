from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import RegistroUsuarioForm, LoginForm
from django.contrib.auth import authenticate, login
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

def registro_usuario(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Registro exitoso! Ahora puedes iniciar sesión.')
            return redirect('registro')  # Redirigir a una página de registro exitoso
    else:
        form = RegistroUsuarioForm()
    
    context = {'form': form}
    return render(request, 'registro.html', context)



def inicio_sesion(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')  # Redirigir a la página de inicio
    else:
        form = LoginForm()
    
    context = {'form': form}
    return render(request, 'login.html', context)
