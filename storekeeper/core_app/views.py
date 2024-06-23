from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    if request.user.role == 'jefe_deposito':
        return redirect('deposito_app:carga_repuestos')
    elif request.user.role == 'jefe_tecnico':
        return redirect('taller_app:gestion_orden_trabajo')
    elif request.user.role == 'gerente_tecnico':
        return redirect('gerencia_app:dashboard_gerencia')
    elif request.user.role == 'operario_deposito':
        return redirect('deposito_app:consulta_repuestos')
    else:
        return redirect('core_app:inicio')