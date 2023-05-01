from django.db import models

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.db import models


from django.dispatch import receiver
# class userExtend(User)

class SignUp(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True,)
    username = models.CharField(max_length=50,null=True,)
    password = models.CharField(max_length=50,null=True,)
    created_date = models.DateTimeField(auto_now_add=True)
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
    
        if created:
            y=SignUp.objects.create(user=instance)
            
            j=User_Details.objects.create(user=y)
            print(j)
           

    # def __str__(self):
    #     return (self.username)
    
# Create your models here.
class User_Details(models.Model):
    user = models.OneToOneField(SignUp, on_delete=models.CASCADE, null=True,)

    fname = models.CharField(max_length=100,null=True,blank=True)
    lname = models.CharField(max_length=100,null=True,blank=True)
    email = models.CharField(max_length=100,null=True,blank=True)
    
    phone_no = models.CharField(max_length=100,null=True,blank=True)

