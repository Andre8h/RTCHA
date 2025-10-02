from django.db import models
from accounts.models import User
# declaring types.
message_type = [("audio","Audio"),("text","Text"),("image","Image")]
status= [("send","Send"),("received","Received"),("read","Read")]

class Message(models.Model):
    id = models.IntegerField(primary_key=True,unique=True)
    message_type = models.CharField(choices=message_type)
    user_sen= models.ForeignKey(User,on_delete=models.CASCADE,related_name="sent_messages")
    user_rec= models.ForeignKey(User, on_delete=models.CASCADE)
    message= models.CharField
    media_url= models.CharField
    sending_date= models.DateTimeField(auto_now=True)
    receiving_date= models.DateTimeField(auto_now=True)
    status= models.CharField(choices=status)

    def display_sender(self):
        if self.user_sen.name == "deleted_user":
            return self.user_sen.email
        return self.user.name