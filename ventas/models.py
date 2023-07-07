from django.db import models
<<<<<<< HEAD

# Create your models here.
    
class Producto(models.Model):
    nombre = models.CharField(max_length=64)
 #  categoria = models.CharField(max_length=32)
    precio = models.IntegerField()
=======
from django.db.models.fields import CharField

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=0)

    def __str__(self):
        return f"Nombre: {self.nombre}, Precio: {self.precio}"
    
class Motos(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
>>>>>>> unreleased

    def __str__(self):
        return f'{self.nombre} -> {self.precio}'
    
# class Producto(models.Model):
#     id = models.AutoField(primary_key=True)
#     detalle_venta = models.ForeignKey('DetalleVenta', on_delete=models.CASCADE)
#     nombre = models.CharField(max_length=100)
#     descripcion = models.CharField(max_length=255)
#     precio = models.DecimalField(max_digits=10, decimal_places=2)

<<<<<<< HEAD
#     def __str__(self):
#         return f'{self.nombre} -> {self.precio}'

# class DetalleProducto(models.Model):
#     id = models.AutoField(primary_key=True)
#     producto = models.ForeignKey('Producto', on_delete=models.CASCADE)
#     cantidad = models.IntegerField()
#     precio = models.DecimalField(max_digits=10, decimal_places=2)
#     fecha_registro = models.DateField()
#     marca = models.CharField(max_length=100)
#     modelo = models.CharField(max_length=100)
#     foto = models.CharField(max_length=255)

#     def __str__(self):
#         return f"DetalleProducto {self.id}"

# # class DetalleVenta(models.Model):
# #     id = models.AutoField(primary_key=True)
# #     venta = models.ForeignKey('Ventas', on_delete=models.CASCADE)
# #     cantidad = models.IntegerField()
# #     precio = models.DecimalField(max_digits=10, decimal_places=2)

# #     def __str__(self):
# #         return f"DetalleVenta {self.id}"

# class Ventas(models.Model):
#     id = models.AutoField(primary_key=True)
#     rut = models.IntegerField()
#     fecha = models.DateField()
#     total = models.DecimalField(max_digits=10, decimal_places=2)

#     def __str__(self):
#         return f"Venta {self.id}"

# class GuiaDespacho(models.Model):
#     id_guia = models.IntegerField(primary_key=True)
#     venta = models.ForeignKey('Ventas', on_delete=models.CASCADE)
#     id_medio_pago = models.IntegerField()
#     neto = models.DecimalField(max_digits=10, decimal_places=2)
#     iva = models.DecimalField(max_digits=10, decimal_places=2)
#     ttpo_documento = models.CharField(max_length=100)
#     tipo_retiro = models.CharField(max_length=100)
#     direccion = models.CharField(max_length=255)

#     def __str__(self):
#         return f"GuiaDespacho {self.id_guia}"

# class MedioPago(models.Model):
#     id_medio_pago = models.IntegerField(primary_key=True)
#     nombre = models.CharField(max_length=100)
#     descripcion = models.CharField(max_length=255)

#     def __str__(self):
#         return self.nombre

# class Descuento(models.Model):
#     id_descuento = models.IntegerField(primary_key=True)
#     nombre = models.CharField(max_length=100)
#     porcentaje = models.DecimalField(max_digits=5, decimal_places=2)
#     descripcion = models.CharField(max_length=255)

#     def __str__(self):
#         return self.nombre

# class Cliente(models.Model):
#     rut = models.CharField(primary_key=True, max_length=20)
#     id_usuario = models.IntegerField()
#     nombre = models.CharField(max_length=100)
#     apellido = models.CharField(max_length=100)
#     sexo = models.CharField(max_length=10)
#     fechanacimiento = models.DateField()
#     direccion = models.CharField(max_length=255)
#     telefono = models.CharField(max_length=20)
#     email = models.CharField(max_length=100)
#     usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)

#     def __str__(self):
#         return f"{self.nombre} {self.apellido}"

# class Usuario(models.Model):
#     id_usuario = models.IntegerField(primary_key=True)
#     tipo_usuario = models.CharField(max_length=100)
#     password = models.CharField(max_length=255)

#     def __str__(self):
#         return f"Usuario {self.id_usuario}"
=======
class Usuario(models.Model):
    rut = models.CharField(max_length=12, primary_key=True)
    nombre_usuario = models.CharField(max_length=100)
    contraseña = models.CharField(max_length=128)
    nombre = models.CharField(max_length=100)
    apellido_paterno = models.CharField(max_length=100)
    apellido_materno = models.CharField(max_length=100)
    email = models.EmailField()
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return self.nombre_usuario

class Ventas(models.Model):
    Boleta = models.IntegerField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    Producto = models.ManyToManyField(Producto, blank=True, related_name='Producto')

    def __str__(self):
        return str(self.Boleta)
>>>>>>> unreleased
