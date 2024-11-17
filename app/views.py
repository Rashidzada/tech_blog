from django.shortcuts import render,redirect
from django.contrib import messages
# Create your views here.
from .import models
def index(request):
    blog = models.Blog.objects.all()
    context = {
        'blogs':blog
    }
    return render(request,'index.html',context)


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        models.Contact.objects.create(name = name , email = email , subject = subject , message = message)
        messages.success(request=request , message=f'Your message was sent successfully thank you!')
        return redirect('index')

    return render(request,'contact.html')