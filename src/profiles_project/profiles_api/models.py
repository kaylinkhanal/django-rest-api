from django.db import models
#abstract base user is the base of the f=django standard user models
from django.contrib.auth.models import AbstractBaseUser,UserManager as AbstractUserManager
#adding permission to spectific users using permission mixins
from django.contrib.auth.models import PermissionsMixin
#class that django uses by default
from django.contrib.auth.models import BaseUserManager

# Create your models here.
class UserManager(AbstractUserManager):
    """Helps Django work with our custom user model"""
    def create_user(self,email,name,password=None):

        if not email:
            raise ValueError('Users must have an email address ')

        email=self.normalize_email(email)
        user=self.model(email=email,name=name)

        user.set_password(password)
        user.save(using=self.db)

        return user

    def create_super_user(self,email,name,password):
        """Creates and saves a superusr with given details"""
        user=self.create_user(email,name,password)

        user.is_superuser=True
        user.is_staff= True

        user.save(using=self._db)
        return user


class UserProfile(AbstractBaseUser):
    """Represents user profile inside our system"""#docstring

    email = models.EmailField(max_length=255,unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField( default=False)

    #object manager to substitute custom models
    objects = UserManager()

    USERNAME_FIELD ='email'
    REQUIRED_FIELD =['name']

    #creating helper function for our models
    def get_full_name(self):
        """Used to get a users full name"""

        return self.name

    def get_short_name(self):
        """Used to get users short name."""

        return self.name

    def __str__(self):
        """Django uses this when it needs to  convert object into a string"""

        return self.email
