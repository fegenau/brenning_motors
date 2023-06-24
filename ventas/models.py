from django.db import models
from django.db.models.fields import CharField

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def str(self):
        return self.nombre

class modelos(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def str(self):
        return self.nombre

class Usuario(models.Model):
    rut = models.IntegerField(primary_key=True)
    tipo_usuario = models.CharField(max_length=100)
    password = models.CharField(max_length=255)

    def str(self):
        return int(self.rut)


class Ventas(models.Model):
    Boleta = models.IntegerField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    Producto = models.ManyToManyField(Producto, blank=True, related_name='Producto')

    def str(self):
        return self.Boleta