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
        subject = request.POST['subject']
        email = request.POST['email']
        message = request.POST['message']
        models.Contact.objects.create(name = name , subject = subject , email= email , message = message)
        messages.success(request=request, message=f'Thank Your message sent to us: {name}')
        return redirect('index')
    return render(request,'contact.html')