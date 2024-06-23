# deposito_app/models.py
from django.db import models

class ItemType(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=100)
    fabricante = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    numero_parte = models.CharField(max_length=20, unique=True)
    costo_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    detalle = models.TextField()
    tipo = models.ForeignKey(ItemType, on_delete=models.CASCADE)

    def __str__(self):
        return self.name