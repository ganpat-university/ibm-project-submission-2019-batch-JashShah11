from django.contrib import admin
from django.contrib.auth import get_user_model 

User = get_user_model() 

# from .models1 import  SignUp,User_Details

admin.site.register(User)

# admin.site.register(User_Details)
# Register your models here.
