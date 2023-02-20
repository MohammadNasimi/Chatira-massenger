from django.db import models
from core.models import BaseModel
# Create your models here.
from django.contrib.auth.models import AbstractUser,UserManager

# json field 
from jsonfield import JSONField


class MyUserManager(UserManager):
    def create_superuser(self, username=None, email=None, password=None, **extra_fields):
        username = extra_fields['phone']
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(username, email, password, **extra_fields)
    def create_user(self, username=None, email=None, password=None, **extra_fields):
        username = extra_fields['phone']
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, email, password, **extra_fields)


class User(AbstractUser):
    phone = models.CharField(max_length=11, null=True, blank=True, unique=True)
    otp = models.PositiveIntegerField(blank=True,null=True)
    otp_create_time = models.DateTimeField(auto_now=True)
    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []
    backend =''


    objects = MyUserManager()
    def __str__(self) -> str:
        return f'{self.phone}'
    
class profile(BaseModel):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    username = models.CharField(max_length=20, null=True, blank=True, unique=True)
    bio = models.TextField(max_length=100, null=True, blank=True)
    profile_pic = models.ImageField(null=True,default=None,upload_to="profile_picture",
                                    max_length=100)
    
    def __str__(self) -> str:
        return f'{self.user.phone ,self.username}'
   
    
def personal_theme_defualt():
    return {"color": "black",
            "theme": "white"}
class user_meta(BaseModel):
    profile = models.OneToOneField(profile,on_delete=models.CASCADE)
    personal_theme = JSONField("personal_theme", default=personal_theme_defualt)
    status = models.BooleanField(null=False,blank=False,default=False)
    last_seen =models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f'{self.profile.user.phone ,self.last_seen}'