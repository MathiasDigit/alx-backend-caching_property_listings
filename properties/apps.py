from django.apps import AppConfig

class PropertiesConfig(AppConfig):
    name = 'properties'

    def ready(self):
        import properties.signals  # Connecte les signaux au démarrage
