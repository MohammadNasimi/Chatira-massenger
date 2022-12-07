from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser,UserManager


class MyUserManager(UserManager):
    def create_superuser(self, username=None, email=None, password=None, **extra_fields):
        username = extra_fields['phone']
        return self._create_user(username, email, password, **extra_fields)


class User(AbstractUser):
    phone = models.CharField(max_length=11, null=True, blank=True, unique=True)
    username = models.CharField(max_length=20, null=True, blank=True, unique=True)
    bio = models.CharField(max_length=20, null=True, blank=True, unique=True)

    USERNAME_FIELD = ['phone']
    objects = MyUserManager()