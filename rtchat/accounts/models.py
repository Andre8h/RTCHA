from django.db import models

# Create your models here.

class User(models.Model):
    id=models.IntegerField(primary_key=True,unique=True)
    created_at = models.DateTimeField(auto_created=True)
    password = models.CharField
    name = models.CharField(max_length=40)
    about = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    profile_photo = models.ImageField

class Contact(models.Model):
    contact_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="contact_user")
    userowner_id = models.ForeignKey(User,on_delete=models.CASCADE, related_name="contactowner_user")
    name = models.CharField(max_length=40)
    blocked = models.BooleanField