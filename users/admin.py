from django.contrib import admin
from django.contrib.auth.admin import UserManager

from .models import User
# Register your models here.

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User

    list_display = ("email", "role", "is_staff", "is_active")

    ordering = ("email")
    search_fields = ("email")

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Role", {"fields": ("role")}),
        ("Permission", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),   
    )

    add_fieldsets = (
        (None, {"classes": ("wide",),
       "fields": ("email", "password1", "password2", "role", "is_staff", "is_superuser" )}),
    )