from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.
#accounts 
from accounts.models import User,profile

admin.site.register(User,UserAdmin)
admin.site.register(profile)