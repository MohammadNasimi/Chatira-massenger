from django.db import models
from core.models import BaseModel
from accounts.models import profile
# Create your models here.
content_massege_type= (
           (1, "text"),
           (2, "image"),
           (3, "video"),
)
class massege(BaseModel):
    sender = models.ForeignKey(profile,on_delete=models.CASCADE,related_name='sender_set')
    reciever=models.ForeignKey(profile,on_delete=models.CASCADE,related_name='reciever_set')
    content=models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    seen_time_stamp = models.DateTimeField(auto_now_add=True)
    content_type =  models.CharField(max_length = 20,choices = content_massege_type,default = 1)
    sender_delete = models.BooleanField(default=False)
    reciver_delete =models.BooleanField(default=False)

    def __str__(self) -> str:
        return {self.sender.user.phone,self.content_type}