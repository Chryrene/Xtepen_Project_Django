# Gestion/apps.py
from django.apps import AppConfig

class GestionConfig(AppConfig):
    name = 'Gestion'

    def ready(self):
        import Gestion.signals
