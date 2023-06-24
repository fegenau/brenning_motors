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
from ventas.views import agregar_producto, eliminar_producto, restar_producto, limpiar_carrito

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('productos/',views.productos),
    path('modelos/',views.modelos),
    path('contacto/',views.contacto),
    path('login/',views.login),
    path('urbanas/',views.urbanas),
    path('hypernaked/',views.hypernaked),
    path('adventuretouring/',views.adventuretouring),
    path('vintage/',views.vintage),
    path('privacy/', views.politicas),
    path('africa-twin/',views.atwin),
    path('super-tenere/',views.suptenere),
    path('tiger/',views.tiger),
    path('agregar/<int:producto_id>/', agregar_producto, name="Add"),
    path('eliminar/<int:producto_id>/', eliminar_producto, name="Del"),
    path('restar/<int:producto_id>/', restar_producto, name="Sub"),
    path('limpiar/', limpiar_carrito, name="CLS"),



#Scooters
    path('scooters/',views.scooters),
        path('VespaPrimavera/',views.VespaPrimavera),
        path('YamahaNMAX/',views.YamahaNMAX),
        path('HondaPCX/',views.HondaPCX),







]
