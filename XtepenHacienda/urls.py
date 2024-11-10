from django.contrib import admin
from django.urls import path, include
from . import views  # Asegúrate de importar las vistas de XtepenHacienda

urlpatterns = [
    path('admin/', admin.site.urls),
    path('gestion/', include('Gestion.urls')),
    path('login/', include('Login.urls')),
    path('', views.home, name='home'),  # Ruta para la página de inicio
]
