from django.urls import path
from.templates.login_app import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
]