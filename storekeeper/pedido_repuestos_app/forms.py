from django import forms
from .models import PedidoRepuesto

class PedidoRepuestoForm(forms.ModelForm):
    class Meta:
        model = PedidoRepuesto
        fields = ('cantidad',)