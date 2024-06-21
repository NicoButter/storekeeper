from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('gerente', 'Gerente'),
        ('jefe_tecnico', 'Jefe Técnico'),
        ('tecnico_senior', 'Técnico Senior'),
        ('tecnico_jr1', 'Técnico JR1'),
        ('tecnico_jr2', 'Técnico JR2'),
        ('gerente_tecnico', 'Gerente Técnico'),
        ('jefe_de_deposito', 'Jefe de Depósito'),
        ('tecnico_deposito', 'Técnico de Depósito'),
        ('operario_deposito', 'Operario de Depósito'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return self.username