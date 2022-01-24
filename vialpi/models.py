from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.utils import timezone


# Create your models here.
class UserManager(BaseUserManager):

    def create_user(self,email,username,Register_as,first_name,last_name,phone_number,password):
            if not username:
                raise ValueError(('The given username must be set'))
            if not email:
                raise ValueError(('Email is required'))
            if not Register_as:
                raise ValueError('You must either register as a buyer or seller')
            if not first_name:
                raise ValueError(('First_name is required'))
            if not last_name:
                raise ValueError(('Last-name is required'))
            if not phone_number:
                raise ValueError(('phone_number is required'))
            user= self.model(
                email=self.normalize_email(email),
                username=username,
                Register_as=Register_as,
                first_name=first_name,
                last_name=last_name,
                phone_number=phone_number
            )

            user.set_password(password)
            user.save(using=self._db)
            return user

    def create_superuser(self,email,username,Register_as,first_name,last_name,phone_number,password):
        user=self.create_user(
             email=self.normalize_email(email),
             username=username,
             Register_as=Register_as,
             first_name=first_name,
             last_name=last_name,
             phone_number=phone_number,
             password=password,
        )

        user.is_admin=True
        user.is_staff=True
        user.is_superuser=True
        user.save(using=self._db)
        return user

            

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=250, unique=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    Register_as=models.CharField(max_length=200,blank=True,null=True)
    phone_number=models.CharField(max_length=300,blank=True,null=True)

    


    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['Register_as','phone_number','username','first_name','last_name'] 



class ContactUs(models.Model):
     full_name=models.CharField(max_length=250)
     email=models.EmailField(max_length=250)
     phone_number=models.CharField(max_length=200)
     your_message=models.TextField()

     def __str__(self):
         return self.email




