from cargar_repuesto_app.models import Repuesto
from django.shortcuts import render, redirect
from .forms import PedidoRepuestoForm

def lista_repuestos_disponibles(request):
    repuestos = Repuesto.objects.all()
    return render(request, 'pedido_repuesto/lista_repuestos_disponibles.html', {'repuestos': repuestos})


def pedido_repuesto_crear(request, repuesto_id):
    repuesto = Repuesto.objects.get(id=repuesto_id)
    if request.method == 'POST':
        form = PedidoRepuestoForm(request.POST)
        if form.is_valid():
            pedido = form.save(commit=False)
            pedido.jefe_tecnico = request.user
            pedido.repuesto = repuesto
            pedido.save()
            return redirect('pedido_repuesto_lista')
    else:
        form = PedidoRepuestoForm()
    return render(request, 'pedido_repuesto/pedido_repuesto_crear.html', {'form': form, 'repuesto': repuesto})