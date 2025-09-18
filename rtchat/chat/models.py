from django.db import models

# declaring types.
message_type = [("audio","Audio"),("text","Text"),("image","Image")]
status= [("send","Send"),("received","Received"),("read","Read")]

class Message(models.Model):
    id = models.IntegerField(primary_key=True,unique=True)
    message_type = models.CharField(choices=message_type)
    user_sen= models.IntegerField
    user_rec= models.IntegerField
    message= models.CharField
    media_url= models.CharField
    sending_date= models.DateTimeField(auto_now=True)
    receiving_date= models.DateTimeField(auto_now=True)
    status= models.CharField(choices=status)