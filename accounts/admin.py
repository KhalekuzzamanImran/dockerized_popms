from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Permission
from django.contrib import admin
from accounts.models import Role, CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('id', 'email',  'full_name', 'contact_number', 'role', 'is_active')
    list_filter = ('email', 'contact_number', 'role', 'is_staff', 'is_active', 'is_superuser',)
    fieldsets = (
        (None, {'fields': ('email', 'full_name', 'contact_number', 'role', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser')}),
        
        ('Group Permissions', {
            'classes': ('collapse',),
            'fields': ('groups', 'user_permissions', )
        })
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email',  'contact_number', 'full_name', 'role', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)

admin.site.register(CustomUser, CustomUserAdmin)


@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
    model = Permission
    fields = ['name', 'key']


admin.site.register(Role)