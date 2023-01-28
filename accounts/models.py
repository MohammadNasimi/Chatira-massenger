from django.db import models
from core.models import BaseModel
# Create your models here.
from django.contrib.auth.models import AbstractUser,UserManager


class MyUserManager(UserManager):
    def create_superuser(self, username=None, email=None, password=None, **extra_fields):
        username = extra_fields['phone']
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(username, email, password, **extra_fields)


class User(AbstractUser):
    phone = models.CharField(max_length=11, null=True, blank=True, unique=True)
    USERNAME_FIELD = 'phone'
    objects = MyUserManager()
    
    def __str__(self) -> str:
        return f'{self.phone}'
    
class profile(BaseModel):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    username = models.CharField(max_length=20, null=False, blank=False, unique=True)
    bio = models.TextField(max_length=100, null=True, blank=True, unique=True)
    profile_pic = models.ImageField(null=True,default=None,upload_to="profile_picture",
                                    max_length=100)
    
    def __str__(self) -> str:
        return f'{self.user.phone ,self.username}'