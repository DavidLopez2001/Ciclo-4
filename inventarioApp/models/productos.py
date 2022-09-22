from django.db import models

class Producto(models.Model):
    id_producto = models.IntegerField()
    nombre_producto = models.CharField(max_length=100)
    vencimiento_producto = models.DateTimeField()
    descripcion_producto = models.CharField(max_length=500)