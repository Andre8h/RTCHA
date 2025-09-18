from django.db import models

role= [("member","Member"),("admin","Admin")]

# Create your models here.
class Group(models.Model):
    id = models.IntegerField(primary_key=True,unique=True)
    group_name = models.CharField
    group_pic = models.ImageField
    admin_id = models.IntegerField
    creation_date = models.DateTimeField(auto_created=True)


class Group_member(models.Model):
    member_id = models.IntegerField(primary_key=True,unique=True)
    group_id = models.IntegerField(unique=True)
    user_id= models.IntegerField
    join_date= models.DateTimeField(auto_created=True)
    role= models.CharField(choices=role)