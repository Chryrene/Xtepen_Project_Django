from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.forms.models import model_to_dict
from .models import Perfil, Reserva, Lugar
from .forms import ReservaForm
from django.views.decorators.http import require_POST

@login_required
def redirect_dashboard(request):
    try:
        perfil = Perfil.objects.get(user=request.user)
        if perfil.rol == 'admin':
            return redirect('admin_dashboard')
        else:
            return redirect('client_dashboard')
    except Perfil.DoesNotExist:
        # Redirige a la página de registro si no se encuentra el perfil
        return redirect('register')

@login_required
def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')

@login_required
def client_dashboard(request):
    return render(request, 'client_dashboard.html')

@login_required
def crear_reserva(request):
    if request.method == "POST":
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('redirect_dashboard')  # Redirige al dashboard
    else:
        form = ReservaForm()
    return render(request, 'reservas/form_reserva.html', {'form': form})

@login_required
def listar_reservas(request):
    reservas = Reserva.objects.all()
    return render(request, 'reservas/lista_reservas.html', {'reservas': reservas})

@login_required
def listar_lugares(request):
    lugares = Lugar.objects.filter(disponible=True)
    return render(request, 'reservas/lista_lugares.html', {'lugares': lugares})

# Vistas para manejar edición y eliminación de lugares en la misma página

@require_POST
@login_required
def api_editar_lugar(request, pk):
    try:
        lugar = Lugar.objects.get(pk=pk)
        # Obtener datos de la solicitud POST
        nuevo_nombre = request.POST.get('nombre')
        nueva_descripcion = request.POST.get('descripcion')
        nueva_capacidad = request.POST.get('capacidad')
        nuevo_disponible = request.POST.get('disponible') == 'true'

        # Actualizar los campos del lugar
        lugar.nombre = nuevo_nombre
        lugar.descripcion = nueva_descripcion
        lugar.capacidad = int(nueva_capacidad)  # Asegurar tipo entero
        lugar.disponible = nuevo_disponible
        lugar.save()

        # Enviar respuesta con los datos actualizados
        return JsonResponse({'status': 'success', 'lugar': model_to_dict(lugar)})
    except Lugar.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Lugar no encontrado'}, status=404)

@require_POST
@login_required
def api_eliminar_lugar(request, pk):
    try:
        lugar = Lugar.objects.get(pk=pk)
        lugar.delete()
        return JsonResponse({'status': 'success', 'id': pk})
    except Lugar.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Lugar no encontrado'}, status=404)

@login_required
def listar_reservas(request):
    reservas = Reserva.objects.all()
    return render(request, 'reservas/lista_reservas.html', {'reservas': reservas})