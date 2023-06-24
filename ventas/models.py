from django.db import models
from django.db.models.fields import CharField

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def str(self):
        return self.nombre
<<<<<<< HEAD
    
class Motos(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
=======

class modelos(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def str(self):
>>>>>>> egenau
        return self.nombre

class Usuario(models.Model):
    rut = models.IntegerField(primary_key=True)
<<<<<<< HEAD
    nombre = models.CharField(max_length=100)
    tipo_usuario = models.CharField(max_length=100)
    password = models.CharField(max_length=255)

    def __str__(self):
        return str(self.rut)
=======
    tipo_usuario = models.CharField(max_length=100)
    password = models.CharField(max_length=255)

    def str(self):
        return int(self.rut)
>>>>>>> egenau


class Ventas(models.Model):
    Boleta = models.IntegerField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    Producto = models.ManyToManyField(Producto, blank=True, related_name='Producto')

<<<<<<< HEAD
    def __str__(self):
        return str(self.Boleta)
=======
    def str(self):
        return self.Boleta
>>>>>>> egenau
