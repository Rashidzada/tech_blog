from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Blog(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    blog_image = models.ImageField(upload_to='blog_images/',blank=True)
    video_url = models.CharField(max_length=233,blank=True, unique=True)
    tags = models.ManyToManyField('Tag')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} By {self.user.username}'
    
class Tag(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title
    

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.name

class FeedBack(models.Model):
    name = models.CharField(max_length=233)
    title = models.CharField(max_length=233)
    content = models.TextField()
    data_file  = models.FileField(upload_to='feedback_files/',blank=True)
    created_at =  models.DateTimeField(auto_now_add=True)
    response = models.TextField(blank=True)


    def __str__(self):
        return self.name 
    

class News(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=200,unique=True)
    content = models.TextField(blank=True)
    image = models.ImageField(upload_to='news_images/',blank=True)
    url = models.URLField(blank=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'{self.title} news uploaded by {self.user.username}'