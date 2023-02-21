from django.apps import AppConfig
from django.core.signals import request_finished
from django.db.models.signals import post_save

class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'
    def ready(self):
        from accounts.signals import my_callback,create_new_user
        from accounts.models import User
        request_finished.connect(my_callback)
        post_save.connect(create_new_user,sender=User)
