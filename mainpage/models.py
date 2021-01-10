from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib import auth

class CustomUserManager(BaseUserManager):
    def create_user(self,username,\
                name,birth,gender,\
                belong, position,address,\
                email,phone,finalEducation,\
                major,password=None,**extra_fields):
        user = self.model(
            username = username, 
            name = name,
            birth = birth,
            gender = gender,
            belong = belong,
            position = position,
            address = address,
            email = email,
            phone = phone,
            finalEducation = finalEducation,
            major = major
            )
        user.is_staff = False
        user.is_superuser = False
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,username,\
                name=None,birth=None,gender=None,\
                belong=None, position=None,address=None,\
                email=None,phone=None,finalEducation=None,\
                major=None,password=None,**extra_fields):
        user = self.create_user(
            username = username,
            password = password,
            name = name,
            birth = birth,
            gender = gender,
            belong = belong,
            position = position,
            address = address,
            email = email,
            phone = phone,
            finalEducation = finalEducation,
            major = major
        )
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.has_perm('mainpage.add_CustomUser')
        user.has_perm('mainpage.change_CustomUser')
        user.has_perm('mainpage.delete_CustomUser')
        user.has_perm('mainpage.view_CustomUser')
        user.save(using=self._db)
        return user
    
    def delete_everything(self):
        CustomUser.objects.all().delete()

# Create your models here.

finalEducationChoices = [
    ('초등학교 졸업','초등학교 졸업'),
    ('중학교 졸업','중학교 졸업'),
    ('고등학교 졸업','고등학교 졸업'),
    ('대학교 졸업','대학교 졸업'),
    ('석사 졸업','석사 졸업'),
    ('박사 졸업','박사 졸업'),
]

class CustomUser(AbstractBaseUser):

    objects = CustomUserManager()

    username = models.CharField(max_length=40, unique=True)
    name = models.CharField(max_length=20, default="", null=True)
    birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=20,choices=[('남성','남성'),('여성','여성')], default="", null=True)
    belong = models.CharField(max_length=30, default="", null=True)
    position = models.CharField(max_length=20, default="", null=True)
    address = models.CharField(max_length=100, default="", null=True)
    email = models.EmailField(max_length=254, default="", null=True)
    phone = models.CharField(max_length=20,default="", null=True)
    finalEducation = models.CharField(max_length=15,choices=finalEducationChoices,default="", null=True)
    major = models.CharField(max_length=100, default="", null=True)

    USERNAME_FIELD = 'username'
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        if self.is_superuser == True:
            return True
        else:
            return False

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        if self.is_superuser == True:
            return True
        else:
            return False
    
    def is_staff(self):
        return self.is_superuser