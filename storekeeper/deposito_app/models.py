from django.shortcuts import render
from cargar_repuesto_app.models import Repuesto  # Import from cargar_repuesto_app

def lista_repuestos(request):
    repuestos = Repuesto.objects.all()
    return render(request, 'deposito/lista_repuestos.html', {'repuestos': repuestos})