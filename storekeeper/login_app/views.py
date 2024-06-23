from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login

def login_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirigir a la página de inicio
            else:
                error = 'Credenciales incorrectas'
                return render(request, 'login.html', {'form': form, 'error': error})
    else:
        form = CustomUserCreationForm()
    return render(request, 'login.html', {'form': form})