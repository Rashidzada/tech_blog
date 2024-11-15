from django.shortcuts import render

# Create your views here.
from .import models
def index(request):
    blog = models.Blog.objects.all()
    context = {
        'blogs':blog
    }
    return render(request,'index.html',context)