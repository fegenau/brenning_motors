from django.db import models

# Create your models here.

class Producto(models.Model):
<<<<<<< HEAD
    titulo = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='productos/')
    precio = models.DecimalField(max_digits=10, decimal_places=2)

=======
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre
    
class Motos(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre

class Usuario(models.Model):
    rut = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    tipo_usuario = models.CharField(max_length=100)
    password = models.CharField(max_length=255)

    def __str__(self):
        return str(self.rut)


class Ventas(models.Model):
    Boleta = models.IntegerField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    Producto = models.ManyToManyField(Producto, blank=True, related_name='Producto')

    def __str__(self):
        return str(self.Boleta)
>>>>>>> unreleased
