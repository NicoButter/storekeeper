from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = [
        ('jefe_tecnico', 'Jefe Técnico'),
        ('jefe_deposito', 'Jefe Deposito'),
        ('gerente_tecnico', 'Gerente Técnico'),
        ('operario_deposito', 'Operario Deposito'),
    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='operario_deposito')