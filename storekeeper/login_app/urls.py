from django.urls import path
from . import views

urlpatterns = [
    # Añade tus rutas aquí
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
]
