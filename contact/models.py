from django.db import models
from core.models import BaseModel
# Create your models here.
from accounts.models import profile
class contact(BaseModel):
    user = models.OneToOneField(profile,on_delete=models.CASCADE)
    contact = models.ForeignKey(profile,on_delete=models.CASCADE)
    block = models.BooleanField(default=False)
    