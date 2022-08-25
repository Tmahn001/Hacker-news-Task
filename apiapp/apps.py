from django.apps import AppConfig


class ApiappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apiapp'

    def ready(self):
        print("starting scheduler")
        from . import news_update
        news_update.startjob()
