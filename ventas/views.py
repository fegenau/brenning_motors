<<<<<<< HEAD
from django.shortcuts import render, HttpResponse, redirect

=======
<<<<<<< HEAD
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import RegistroUsuarioForm,LoginForm
from .models import Usuario,Producto
=======
from django.shortcuts import render,redirect
>>>>>>> egenau
from django.contrib import messages
from .forms import RegistroUsuarioForm, LoginForm
from django.contrib.auth import authenticate, login
>>>>>>> unreleased
# Create your views here.
 
from ventas.Carrito import Carrito
from ventas.models import Producto


def tienda(request):
    productos = Producto.objects.all()
    return render(request, "productos.html", {'productos':productos})

def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect("Productos")

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect("Productos")

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect("Productos")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("Productos")

def index(request):
    return render(request, 'index.html')

def productos(request):
    return render(request, 'productos.html')

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
    
<<<<<<< HEAD
    return render(request, 'login.html', {'form': form})


def carrito_compras(request):
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
            'subtotal': subtotal
        })

        # Calcular el total de la compra
        total += subtotal

    return render(request, 'ShoppingCart/carrito.html', {'detalles_carrito': detalles_carrito, 'total': total})

def agregar_producto(request, producto_id):
    # Obtener el producto desde la base de datos
    producto = get_object_or_404(Producto, pk=producto_id)

    # Obtener el carrito actual del usuario desde la sesión
    carrito = request.session.get('carrito', {})

    # Incrementar la cantidad del producto en el carrito
    carrito[producto_id] = carrito.get(producto_id, 0) + 1

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
   
=======
    context = {'form': form}
    return render(request, 'login.html', context)
>>>>>>> egenau
