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

def hyperNaked (request):
    return render(request, 'hyperNaked.html')

def cb190 (request):
    return render(request, 'cb190.html')