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
    #campos de texto
    rut = models.CharField(max_length=13, primary_key=True)
    nombre_usuario = models.CharField(max_length=30,default="")
    nombre = models.CharField(max_length=50)
    apellido_paterno = models.CharField(max_length=50,default="")
    apellido_materno = models.CharField(max_length=50,default="")
    email = models.EmailField(default='a@mail.com')
    fecha_nacimiento = models.DateField(default="")
    esta_activa = models.BooleanField(default=True)

    def __str__(self):
        return str(self.nombre_usuario)


class Ventas(models.Model):
    Boleta = models.IntegerField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    Producto = models.ManyToManyField(Producto, blank=True, related_name='Producto')

    def __str__(self):
        return str(self.Boleta)
