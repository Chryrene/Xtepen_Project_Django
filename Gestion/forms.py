from django import forms
from .models import Reserva

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['user', 'fecha_reserva', 'hora_reserva', 'tipo_reserva', 'estado', 'tipo_banquete', 'numero_invitados', 'lugares_disponibles', 'lugar']
        widgets = {
            'fecha_reserva': forms.SelectDateWidget(),  # Usa un calendario
            'hora_reserva': forms.TimeInput(attrs={'type': 'time'}),
        }
