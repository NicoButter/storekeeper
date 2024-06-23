from django import forms
from django.contrib.auth.models import User

class CustomUserCreationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'role')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'role': forms.Select(attrs={'class': 'form-control'})
        }