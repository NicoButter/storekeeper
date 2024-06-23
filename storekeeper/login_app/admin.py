from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm
from .models import User

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    list_display = ('username', 'email', 'role')
    list_filter = ('role',)
    search_fields = ('username', 'email')

admin.site.register(User, CustomUserAdmin)