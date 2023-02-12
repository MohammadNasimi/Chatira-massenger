from django.db import models
from core.models import BaseModel
# Create your models here.
from accounts.models import profile
class contact(BaseModel):
    user = models.ForeignKey(profile,on_delete=models.CASCADE,related_name='user_set')
    name_contact = models.CharField(max_length=20)
    contact = models.ForeignKey(profile,on_delete=models.CASCADE,related_name='contact_set')
    block = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.user.user.phone