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