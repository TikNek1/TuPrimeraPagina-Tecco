from django.urls import path
from . import views

urlpatterns = [
    path('', views.bienvenida, name='bienvenida'),
    # path('', views.listar_viajes, name='listar_viajes'),
    path('viajes/', views.listar_viajes, name='listar_viajes'),
    path('guias/', views.lista_guias, name='listar_guias'),
    path('pilotos/', views.lista_pilotos, name='listar_pilotos'),
    path('viaje/<int:viaje_id>/', views.detalle_viaje, name='detalle_viaje'),
    path('nuevo_viaje/', views.crear_viaje, name='crear_viaje'),
]