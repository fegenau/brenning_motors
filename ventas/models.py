from django.db import models

# Create your models here.

class Producto(models.Model):
    titulo = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='productos/')
    precio = models.DecimalField(max_digits=10, decimal_places=2)

