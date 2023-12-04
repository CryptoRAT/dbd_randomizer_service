from django.contrib import admin

from user.models import RegisteredUser


# Register your models here.
class RegisteredUserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'is_staff', 'is_active')

# Register your models here.

admin.site.register(RegisteredUser, RegisteredUserAdmin)
