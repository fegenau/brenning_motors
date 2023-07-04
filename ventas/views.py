from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import Producto
from django.shortcuts import render

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

#hyperNaked
def hyperNaked (request):
    return render(request, 'hyperNaked.html')

def cb190 (request):
    return render(request, 'cb190.html')

def mT07 (request):
    return render(request, 'mT07.html')

def streetTripleRS (request):
    return render(request, 'streetTripleRS.html')

def g310r (request):
    return render(request, 'G310R.html')

def fz25 (request):
    return render(request, 'fz25.html')

def xr (request):
    return render(request, 'xr.html')

def productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos.html', {'productos': productos})

def productos(request):
    # Agregar los productos a la base de datos
    Producto.objects.create(titulo="Guantes", imagen="imgs/guantes.jpg", precio=20000)
    Producto.objects.create(titulo="Botas", imagen="imgs/botas.jpg", precio=140000)
    Producto.objects.create(titulo="Chaqueta", imagen="imgs/chaqueta.jpg", precio=200000)
    Producto.objects.create(titulo="Mochila", imagen="imgs/mochila.jpg", precio=110000)

    # Obtener todos los productos de la base de datos
    productos = Producto.objects.all()
    return render(request, 'productos.html', {'productos': productos})
