from django.contrib import admin
from .models import EquipoElectronico

@admin.register(EquipoElectronico)
class EquipoElectronicoAdmin(admin.ModelAdmin):
    list_display = ('equipo', 'precio_venta', 'garantia_activa')
    search_fields = ('equipo', 'marca_specs')
    list_filter = ('garantia_activa',)