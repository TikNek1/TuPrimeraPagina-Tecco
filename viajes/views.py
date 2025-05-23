from django.shortcuts import render, redirect, get_object_or_404
from .models import Viaje, Guia, PilotoCliente
from .forms import ViajeForm
from django.db.models import Q
from datetime import datetime

def bienvenida(request):
    return render(request, 'bienvenida.html')

# Vista para listar todos los viajes
# def listar_viajes(request):
#     viajes = Viaje.objects.all()
#     return render(request, 'viajes/lista_viajes.html', {'viajes': viajes})

# Vista para listar viajes con búsqueda

def listar_viajes(request):
    destino = request.GET.get('destino', '')
    mes = request.GET.get('mes', '')  # formato esperado: YYYY-MM

    viajes = Viaje.objects.all()

    if destino:
        viajes = viajes.filter(destino__icontains=destino)

    if mes:
        try:
            fecha_inicio = datetime.strptime(mes, "%Y-%m")
            fecha_fin = datetime(fecha_inicio.year, fecha_inicio.month + 1, 1) if fecha_inicio.month < 12 else datetime(fecha_inicio.year + 1, 1, 1)
            viajes = viajes.filter(fecha__gte=fecha_inicio, fecha__lt=fecha_fin)
        except ValueError:
            pass  # si el mes viene mal formateado, no se filtra por fecha

    return render(request, 'viajes/lista_viajes.html', {
        'viajes': viajes.order_by('fecha'),
    })

# Vista para ver los detalles de un viaje
def detalle_viaje(request, viaje_id):
    viaje = get_object_or_404(Viaje, id=viaje_id)
    return render(request, 'viajes/detalle_viaje.html', {'viaje': viaje})

# Vista para crear un nuevo viaje
def crear_viaje(request):
    if request.method == 'POST':
        form = ViajeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_viajes')
    else:
        form = ViajeForm()
    
    return render(request, 'viajes/crear_viaje.html', {'form': form})

# Vista para listar guías
def lista_guias(request):
    guias = Guia.objects.all()
    return render(request, 'viajes/lista_guias.html', {'guias': guias})

# Vista para listar pilotos
def lista_pilotos(request):
    pilotos = PilotoCliente.objects.all()
    return render(request, 'viajes/lista_pilotos.html', {'pilotos': pilotos})

