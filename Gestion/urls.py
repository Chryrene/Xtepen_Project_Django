from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/admin/', views.admin_dashboard, name='admin_dashboard'),
    path('dashboard/client/', views.client_dashboard, name='client_dashboard'),
    path('dashboard/', views.redirect_dashboard, name='redirect_dashboard'),
    path('reservas/', views.listar_reservas, name='lista_reservas'),
    path('lugares/', views.listar_lugares, name='lista_lugares'),  # Cambié la ruta a 'lugares/'
    path('reservas/nueva/', views.crear_reserva, name='crear_reserva'),
    path('api/lugares/editar/<int:pk>/', views.api_editar_lugar, name='api_editar_lugar'),
    path('api/lugares/eliminar/<int:pk>/', views.api_eliminar_lugar, name='api_eliminar_lugar'),
]
