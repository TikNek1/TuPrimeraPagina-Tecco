from django.contrib import admin
from .models import Guia, PilotoCliente, Viaje

@admin.register(Guia)
class GuiaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'dni', 'email', 'telefono')

@admin.register(PilotoCliente)
class PilotoClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'dni', 'email', 'telefono')

@admin.register(Viaje)
class ViajeAdmin(admin.ModelAdmin):
    list_display = ('destino', 'fecha', 'kilometros', 'dificultad', 'guia')
    filter_horizontal = ('pilotos',)