from django.contrib.auth.backends import ModelBackend
from accounts.models import User

class phonebackend(ModelBackend):
    """
    Custom authentication backend.

    Allows users to log in using their phone number.
    """
    def authenticate(self, request, username=None, password=None,**kwargs):
        """
        Overrides the authenticate method to allow users to log in using their phone number.
        """
        phone = kwargs["phone"]
        try:
            user = User.objects.get(phone=phone)
            return user
        except User.DoesNotExist:
            return None
