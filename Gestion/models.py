from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rol = models.CharField(max_length=10, choices=[('admin', 'Admin'), ('cliente', 'Cliente')])

    def __str__(self):
        return f"{self.user.username} - {self.rol}"

class Lugar(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    capacidad = models.PositiveIntegerField()  # Capacidad máxima del lugar
    disponible = models.BooleanField(default=True)  # Indica si el lugar está disponible

    def __str__(self):
        return self.nombre

class Reserva(models.Model):
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('confirmada', 'Confirmada'),
        ('cancelada', 'Cancelada')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_reserva = models.DateField()
    hora_reserva = models.TimeField()  # Campo para la hora de la reserva
    tipo_reserva = models.CharField(max_length=50)
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='pendiente')
    
    # Campos para banquetes
    tipo_banquete = models.CharField(max_length=50, blank=True, null=True)
    numero_invitados = models.PositiveIntegerField(blank=True, null=True)
    
    # Relación con lugares de renta
    lugar = models.ForeignKey(Lugar, on_delete=models.CASCADE, null=True, blank=True)

    lugares_disponibles = models.PositiveIntegerField(default=0)  # Control de disponibilidad de lugares

    def __str__(self):
        return f"Reserva de {self.user.username} el {self.fecha_reserva} a las {self.hora_reserva} en {self.lugar.nombre}"
