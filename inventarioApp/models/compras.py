from django.db import models

from inventarioApp.models.clientes import Cliente
from .clientes import Cliente

class Compra(models.Model):
    nombre_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    valor_total = models.PositiveBigIntegerField()
    fecha_compra = models.DateField()
    producto = models.CharField(max_length=100)

    def __str__(self):
        return self.producto