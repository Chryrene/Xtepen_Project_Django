from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Perfil

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
