from django.contrib import admin
from .models import User
# Register your models here.

class UserAdmin(admin.ModelAdmin):

    def full_name(self, obj):
        return obj.get_full_name()

    list_display = ['full_name', 'email', 'is_active', 'is_staff', 'is_superuser']

admin.site.register(User, UserAdmin)