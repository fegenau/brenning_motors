from django.db import models
from django.db.models.fields import CharField

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def str(self):
        return self.nombre
    
class Motos(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre

class Usuario(models.Model):
    rut = models.CharField(max_length=12, primary_key=True)
    nombre_usuario = models.CharField(max_length=100)
    contraseña = models.CharField(max_length=128)
    nombre = models.CharField(max_length=100)
    apellido_paterno = models.CharField(max_length=100)
    apellido_materno = models.CharField(max_length=100)
    email = models.EmailField()
    fecha_nacimiento = models.DateField()
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre_usuario


class Ventas(models.Model):
    Boleta = models.IntegerField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    Producto = models.ManyToManyField(Producto, blank=True, related_name='Producto')

    def __str__(self):
        return str(self.Boleta)
