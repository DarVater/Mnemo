from django.apps import AppConfig


class BaseConnectConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'base_connect'
