from django.contrib import admin

from .models.clientes import Cliente
from .models.compras import Compra
from .models.productos import Producto

# Register your models here.

admin.site.register(Cliente)
admin.site.register(Compra)
admin.site.register(Producto)
