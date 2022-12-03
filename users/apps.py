from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'
    
    #AKI inicia as signals (eventos)
    def ready(self):
        import users.signals


        