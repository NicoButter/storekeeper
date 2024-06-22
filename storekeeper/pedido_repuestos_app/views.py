from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from.forms import PedidoRepuestoForm 
from django.core.paginator import Paginator
from .models import PedidoRepuesto


@login_required
def crear_pedido(request):
    if request.method == 'POST':
        form = PedidoRepuestoForm(request.POST)
        if form.is_valid():
            pedido = form.save(commit=False)
            pedido.jefe_tecnico = request.user
            pedido.save()
            # Enviar email de confirmación de pedido
            # ...
            return redirect('pedido_lista')
    else:
        form = PedidoRepuestoForm()
    return render(request, 'pedido_repuesto/crear_pedido.html', {'form': form})

@login_required
def lista_pedidos(request):
    pedidos = PedidoRepuesto.objects.all()
    paginator = Paginator(pedidos, 10)  # Mostrar 10 pedidos por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'pedido_repuesto/lista_pedidos.html', {'page_obj': page_obj})

def lista_repuestos_disponibles(request):
    # código para mostrar la lista de repuestos disponibles
    return render(request, 'pedido_repuestos_app/lista_repuestos_disponibles.html')