from django.db import models
from django.contrib.auth.models import User
# Create your models here.
''' username, eamil , password , conf'''


class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    address = models.CharField(max_length=200,blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics/',blank=True)

    def __str__(self):
        return f'{self.user.username} - Profile'

