from django.apps import AppConfig


class TratamientoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Tratamiento'

    def ready(self):
        import Tratamiento.signals
