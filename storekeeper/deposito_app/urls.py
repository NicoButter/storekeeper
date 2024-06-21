from django.urls import path
from. import views

urlpatterns = [
    path('lista_repuestos/', views.lista_repuestos, name='lista_repuestos')
]