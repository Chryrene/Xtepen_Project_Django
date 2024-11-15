# Login/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.csrf import csrf_protect
from .forms import RegisterForm
from Gestion.models import Perfil

@csrf_protect
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('redirect_dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            Perfil.objects.create(user=user, rol='cliente')
            login(request, user)
            return redirect('redirect_dashboard')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})
