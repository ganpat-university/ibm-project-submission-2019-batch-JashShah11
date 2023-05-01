from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

class CustomUserManager(BaseUserManager):

    def _create_user(self, username,email,password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        print("Username",username)
        user = self.model(username=username, email=email)
        
        user = self.model(username=username,email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        

    def create_user(self, username,email,password=None, **extra_fields):
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(username,email,password, **extra_fields)

    def create_superuser(self, username,email,password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(
                "Superuser must have is_staff=True."
            )
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(
                "Superuser must have is_superuser=True."
            )

        return self._create_user(username,email,password, **extra_fields)

class CustomUser(AbstractBaseUser,PermissionsMixin):
    username=models.CharField(max_length=50,unique=True)
    email = models.EmailField(max_length=20)
    mobile_num= models.CharField(max_length=20)
    
    
    is_staff = models.BooleanField(default=False)
    is_superuser= models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    date_joined = models.DateTimeField(default=timezone.now)
    

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ['email']

    objects = CustomUserManager()

    # def __str__(self):
    #     return self.username
    


