# Register your models here.
from django.contrib import admin
from .models import * 


class EquiposAdmin(admin.ModelAdmin):
    list_display = [field.name for field in  Equipos._meta.fields]
admin.site.register(Equipos, EquiposAdmin)

# Register your models here.
