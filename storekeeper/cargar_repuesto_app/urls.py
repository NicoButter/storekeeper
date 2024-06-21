from django.urls import path
from . import views

urlpatterns = [
    path('cargar_repuesto/', views.cargar_repuesto, name='cargar_repuesto'),
]