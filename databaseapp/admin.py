from django.contrib import admin
from .models import *
# Register your models here.

class employeeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Employee,employeeAdmin)