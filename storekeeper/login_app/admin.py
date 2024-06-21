from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser

class CustomUserAdmin(BaseUserAdmin):
    # Campos a mostrar en la lista de usuarios
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'role')
    # Campos por los que se puede filtrar en la lista de usuarios
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups', 'role')
    # Campos a editar en el panel de detalles del usuario
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'role')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    # Campos a mostrar en el formulario de creación de usuario
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_staff', 'is_superuser', 'is_active', 'role')}
        ),
    )
    # Campos por los que se puede buscar en el administrador de usuarios
    search_fields = ('username', 'email', 'first_name', 'last_name')
    # Orden por defecto en la lista de usuarios
    ordering = ('username',)

# Registrar el modelo CustomUser con el administrador personalizado CustomUserAdmin
admin.site.register(CustomUser, CustomUserAdmin)
