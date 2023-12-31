"""
URL configuration for Brenning project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ventas import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('productos/',views.productos),
    path('modelos/',views.modelos),
    path('login/',views.inicio_sesion),
    path('urbanas/',views.urbanas),
    path('hyperNaked/',views.hyperNaked),
    path('adventuretouring/',views.adventuretouring),
    path('vintage/',views.vintage),
    path('africa-twin/',views.atwin),
    path('super-tenere/',views.suptenere),
    path('tiger/',views.tiger),
    path('g310r/',views.g310r),
    path('fz25/',views.fz25),
    path('cb190/',views.cb190),
	path('xr/', views.xr),

    #Scooters
    path('scooters/',views.scooters),
    path('VespaPrimavera/',views.VespaPrimavera),
    path('YamahaNMAX/',views.YamahaNMAX),
    path('HondaPCX/',views.HondaPCX),

    #Contacts
    path('contacto/',views.contacto),
    path('privacy/', views.politicas),

    path('registro/',views.registro_usuario),
    path('caferacer/',views.caferacer),
    path('ducati1100/',views.ducati1100),
    path('z650/',views.z650),


    #ShoppingCart
    path('carrito/', views.carrito_compras, name='carrito_compras'),
    path('carrito/agregar/<int:producto_id>/', views.agregar_producto, name='agregar_producto'),
    path('carrito/checkout/', views.checkout, name='checkout'),
    path('carrito/eliminar/<int:producto_id>/', views.eliminar_producto, name='eliminar_producto'),

]
