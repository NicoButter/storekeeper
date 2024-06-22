from django.db import models

class Repuesto(models.Model):
    nombre = models.CharField(max_length=255)
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    numero_parte = models.CharField(max_length=50)
    numero_serie = models.CharField(max_length=50)
    descripcion = models.TextField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    fabricante = models.CharField(max_length=100)
    distribuidor = models.CharField(max_length=100)
    fecha_ingreso
    qr
    tipo
    costo
    detalle
    # imagen
    # otros campos que se definan luego...