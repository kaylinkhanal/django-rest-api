from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

class Student(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)

class ProfileFeedItem(models.Model):
    """Profile status update"""
    user_profile= models.ForeignKey('User',on_delete=models.CASCADE)
    status_text = models.CharField(max_length=255)
    created_on =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return the model as a string"""

        return self.status_text
