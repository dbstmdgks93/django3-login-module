from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class CustomUserManager(BaseUserManager):
    def create_user(self,username,email=None,\
            name=None,birth=None,gender=None,password=None, **extra_fields):
        user = self.model(
            username = username, 
            name = name,
            birth = birth,
            gender = gender)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,username,email=None,\
            name=None,birth=None,gender=None,password=None, **extra_fields):
        user = self.model(
            username = username,
            password = password,
            name = name,
            birth = birth,
            gender = gender
        )
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

# Create your models here.

class CustomUser(AbstractBaseUser):

    objects = CustomUserManager()

    username = models.CharField(max_length=40, unique=True)
    name = models.CharField(max_length=20)
    birth = models.CharField(max_length=20)
    gender = models.CharField(max_length=20)

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username