from django.contrib import admin
from .models import Mymodel

# Register your models here.

class MymodelAdmin(admin.ModelAdmin):
    class Meta:
        model=Mymodel
        field='__all__'

admin.site.register(Mymodel)