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
    
    @property
    def showdateinfo(self):
        return f'{self.created_at} || {self.title}'
    
    
    @property
    def name_title(self):
        return f'{self.title} by {self.name}'

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
    

class Student(models.Model):
    name = models.CharField(max_length=22)
    eng = models.IntegerField()
    urd = models.IntegerField()
    total_marks = models.IntegerField(editable=False, blank=True, null=True)
    average_marks = models.FloatField(editable=False, blank=True, null=True)
    percentage = models.FloatField(editable=False, blank=True, null=True)
    grade = models.CharField(max_length=1, editable=False, blank=True, null=True)
    remarks = models.CharField(max_length=10, editable=False, blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Calculations before saving
        self.total_marks = self.eng + self.urd
        self.average_marks = round(self.total_marks / 2, 2)
        self.percentage = round((self.total_marks / 200) * 100, 2)  # Assuming each subject has 100 marks
        self.grade = 'A' if self.average_marks >= 80 else 'B' if self.average_marks >= 60 else 'C' if self.average_marks >= 40 else 'F'
        self.remarks = 'Passed' if self.percentage >= 50 else 'Failed'
        super().save(*args, **kwargs)

class Info(models.Model):
    first_name  = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

    def __str__(self):
        return self.first_name
    

    def full_name(self):
        full =self.first_name +'-'+ self.last_name
        return full.upper()

