from django.apps import AppConfig


class MmsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.mms'

    def ready(self):
        import apps.mms.signals
