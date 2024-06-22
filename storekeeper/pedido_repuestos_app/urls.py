from django.urls import path
from. import views

urlpatterns = [
    path('lista_repuestos_disponibles/', views.lista_repuestos_disponibles, name='lista_repuestos_disponibles'),
    path('crear/<int:repuesto_id>/', views.crear_pedido, name='crear_pedido')
]