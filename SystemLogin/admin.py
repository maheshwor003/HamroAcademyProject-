from django.contrib import admin
from .models import Homedetails, User


class AdminUser(admin.ModelAdmin):
    list_display = ('username', 'is_staff', 'first_name', 'last_name',
                    'address', 'email', 'is_admin', 'is_student', 'is_teacher')


admin.site.register(User, AdminUser)

admin.site.register(Homedetails)
