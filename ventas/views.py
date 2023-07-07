from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import RegistroUsuarioForm,LoginForm
from .models import Usuario,Producto
from django.contrib import messages
from django.contrib.auth import login, logout
import locale


# Create your views here.

def index(request):
    return render(request, 'index.html')

def productos(request):
    return render(request, 'Products/productos.html')

def modelos(request):
    return render(request, 'modelos.html')

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



def atwin(request):
    return render (request, 'africa-twin.html')

def suptenere(request):
    return render (request, 'super-tenere.html')

def tiger(request):
    return render(request, 'tiger.html')

#Contacts
def contacto(request):
    return render(request, 'Contacts/contacto.html')

def politicas (request):
    return render(request, 'Contacts/privacy-policy.html')


#scooters
def scooters (request):
    return render(request, 'Models/Scooters/scooters.html')

def VespaPrimavera(request):
    return render(request, 'Models/Scooters/VespaPrimavera.html')

def HondaPCX(request):
    return render(request, 'Models/Scooters/HondaPCX.html')

def YamahaNMAX(request):
    return render(request, 'Models/Scooters/YamahaNMAX.html')


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
            usuario = form.save()
            messages.success(request,'Registro existoso')
            return redirect('/') 
    else:
        form = RegistroUsuarioForm()
    
    return render(request, 'formulario-registro.html', 
                  {'form': form
                   })

def login (request):   
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            rut = form.cleaned_data['rut']
            password = form.cleaned_data['password']
            try:
                usuario = Usuario.objects.get(rut=rut, password=password)
                # Guardar información de sesión para el usuario
                request.session['usuario_rut'] = usuario.rut
                request.session['usuario_nombre'] = usuario.nombre
                messages.success(request, 'Inicio de sesión exitoso.')
                return redirect('/')
            except Usuario.DoesNotExist:
                messages.error(request, 'Credenciales inválidas.')
    else:
        form = LoginForm()
    
    return render(request, 'login.html', {'form': form})


def carrito_compras(request):
    # Establecer la configuración local para formatear los números
    locale.setlocale(locale.LC_ALL, 'es_CL.UTF-8')  # Configuración local para Chile

    # Obtener los productos en el carrito del usuario
    carrito = request.session.get('carrito', {})
    
    # Crear una lista para almacenar los detalles de los productos en el carrito
    detalles_carrito = []
    total = 0

    for producto_id, cantidad in carrito.items():
        # Obtener el producto desde la base de datos
        producto = get_object_or_404(Producto, pk=producto_id)

        # Calcular el subtotal del producto
        subtotal = producto.precio * cantidad

        # Agregar los detalles del producto al carrito
        detalles_carrito.append({
            'producto': producto,
            'cantidad': cantidad,
            'subtotal': locale.currency(subtotal, grouping=True)  # Formatear el subtotal como una moneda local con separadores de miles
        })

        # Calcular el total de la compra
        total += subtotal

    # Formatear el total como una moneda local con separadores de miles
    total_formateado = locale.currency(total, grouping=True)

    return render(request, 'ShoppingCart/carrito.html', {'detalles_carrito': detalles_carrito, 'total': total_formateado})

def agregar_producto(request, producto_id):
    # Obtener el producto desde la base de datos
    producto = get_object_or_404(Producto, pk=producto_id)

    # Obtener el carrito actual del usuario desde la sesión
    carrito = request.session.get('carrito', {})

    # Obtener la cantidad ingresada por el usuario en el formulario
    cantidad = int(request.POST.get('cantidad', 1))

    # Verificar si el producto ya está en el carrito
    if producto_id in carrito:
        # Si el producto ya está en el carrito, incrementar la cantidad
        carrito[producto_id] += cantidad
    else:
        # Si el producto no está en el carrito, agregarlo con la cantidad ingresada
        carrito[producto_id] = cantidad

    # Guardar el carrito actualizado en la sesión
    request.session['carrito'] = carrito

    return render(request, 'ShoppingCart/agregar_producto.html', {'producto': producto})

def checkout(request):
    # Obtener el carrito actual del usuario desde la sesión
    carrito = request.session.get('carrito', {})

    # Realizar la lógica de checkout, como cálculos de precios, validaciones, etc.

    # Limpiar el carrito después de completar el checkout
    request.session['carrito'] = {}

    return render(request, 'ShoppingCart/checkout.html')

   