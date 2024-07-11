from django.apps import AppConfig


class TapConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tap'

    def ready(self):
        import tap.signals