from django.shortcuts import render
from.forms import RepuestoForm

def cargar_repuesto(request):
    if request.method == 'POST':
        form = RepuestoForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'core_app/repuesto_cargado.html', {'mensaje': 'Repuesto cargado con éxito'})
    else:
        form = RepuestoForm()
    return render(request, 'core_app/cargar_repuesto.html', {'form': form})

from django.shortcuts import render
from.models import Repuesto

def lista_repuestos(request):
    repuestos = Repuesto.objects.all()
    return render(request, 'deposito/lista_repuestos.html', {'repuestos': repuestos})