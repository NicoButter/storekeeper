from django.db import models

class Repuesto(models.Model):
    TIPO_CHOICES = [
        ('boton', 'Botón'),
        ('fuente_alimentacion', 'Fuente de Alimentación'),
        ('display', 'Display'),
        ('tira_led', 'Tira de LED'),
        ('placa_comunicacion', 'Placa de Comunicación'),
        
    ]
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    marca = models.CharField(max_length=50)
    numero_parte = models.CharField(max_length=50)
    numero_serie = models.CharField(max_length=50)
    detalle = models.TextField()
    qr = models.CharField(max_length=50)
    fecha_ingreso = models.DateField()
    costo_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    