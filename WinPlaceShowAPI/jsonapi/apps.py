from django.apps import AppConfig


class JsonapiConfig(AppConfig):
    name = 'jsonapi'

    def ready(self):
        # Makes sure all signal handlers are connected
        from . import views  # noqa
