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



def feedback(request):
    if request.method == 'POST':
        name = request.POST['name']
        title = request.POST['title']
        content = request.POST['content']
        data_file = request.FILES['data_file']
        models.FeedBack.objects.create(name = name ,title = title ,content = content , data_file = data_file)
        messages.success(request=request , message=f'Your feed back is sended..')
        return redirect('index')
    
    return render(request, 'feedback.html')




def display_feed_back(request):
    feedback = models.FeedBack.objects.all()
    context = {
        'feedbacks':feedback
    }
    return render(request,'display_feed_back.html',context)