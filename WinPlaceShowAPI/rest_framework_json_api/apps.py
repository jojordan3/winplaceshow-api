from django.apps import AppConfig


class RestJSONConfig(AppConfig):
    name = 'rest_framework_json_api'
    verbose_name = "Django REST framework for JSON API"

    from . import views, settings, mixins, metadata, exceptions, serializers