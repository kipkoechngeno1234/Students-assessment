from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Assessment, Submission


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
	pass


admin.site.register(Assessment)
admin.site.register(Submission)
