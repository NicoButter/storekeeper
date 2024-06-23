# deposito_app/forms.py
from django import forms
from.models import Item, ItemType

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'fabricante', 'arca', 'numero_parte', 'costo_unitario', 'detalle', 'tipo')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tipo'].queryset = ItemType.objects.all()