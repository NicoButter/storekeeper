from django.urls import path
from. import views

urlpatterns = [
    path('lista_repuestos_disponibles/', views.lista_repuestos_disponibles, name='lista_repuestos_disponibles'),
    path('crear/<int:repuesto_id>/', views.pedido_repuesto_crear, name='pedido_repuesto_crear')
]