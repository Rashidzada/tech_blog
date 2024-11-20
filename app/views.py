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



def add_news(request):
    if request.method == 'POST':
        user = request.user
        title = request.POST['title']
        content = request.POST['content']
        image = request.FILES.get('image','')
        url = request.POST['url']
        models.News.objects.create(user = user , title = title , content = content , image = image, url = url)
        return redirect('news_list')
    return render(request,'add_news.html')



def news_list(request):
    news = models.News.objects.all()
    context = {
        'news_list':news
    }
    return render(request,'news_list.html',context)


def news_detail(request,news_id):
    news  = models.News.objects.get(id = news_id)
    context = {
        'news':news
    }
    return render(request,'news_detail.html',context)



def delete_news(request,news_id):
    news = models.News.objects.get(id = news_id)
    news.delete()
    messages.success(request=request , message= f'Your news deleted successfully :{news.title}?')
    return redirect('news_list')