from django.shortcuts import render
from .models import Repuesto

def lista_repuestos(request):
    repuestos = Repuesto.objects.all()
    return render(request, 'cargar_repuesto/lista_repuestos.html', {'repuestos': repuestos})