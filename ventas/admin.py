from django.contrib import admin
<<<<<<< HEAD
from .models import Producto
# Register your models here.

admin.site.register(Producto)
=======
from .models import *

# Register your models here.


admin.site.register(Usuario)
admin.site.register(Motos)
admin.site.register(Ventas)
admin.site.register(Producto)

>>>>>>> unreleased
