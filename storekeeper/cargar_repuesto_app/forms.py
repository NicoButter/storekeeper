from django import forms
from.models import Repuesto

class RepuestoForm(forms.ModelForm):
    class Meta:
        model = Repuesto
        fields = ('tipo', 'marca', 'numero_parte', 'numero_serie', 'detalle', 'qr', 'fecha_ingreso', 'costo_unitario')