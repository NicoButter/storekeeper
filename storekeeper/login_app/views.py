from django.shortcuts import render

def login_view(request):
    return render(request, 'login_app/login.html')

def register_view(request):
    return render(request, 'login_app/register.html')