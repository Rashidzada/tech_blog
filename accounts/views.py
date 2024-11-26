from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            if User.objects.filter(username = username).exists():
                messages.warning(request=request,message=f'Username taken')
            elif User.objects.filter(email = email).exists():
                messages.warning(request=request,message=f'Email already registered try othethen: {email}')
            else:
                User.objects.create_user(username=username,email= email ,password=password , is_staff = True)
                #  simple user create and then rediret to the login page for login
                # messages.success(request=request,message=f'You are registred with us thank you:username: {username}: password: {password}')
                # return redirect('login_view')

                # if we want that user created and at that time also login
                user = authenticate(username = username, password = password)
                login(request=request,user=user)
                messages.success(request=request,message=f'You are registred with us thank you:username: {username}: password: {password}')
                return redirect('dashbaord')
        else:
            messages.warning(request=request,message=f'password not matached')
    return render(request,'signup.html')





def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username , password = password)
        if user is not None:
            login(request= request , user=user)
            return redirect('dashbaord')
        else:
            messages.warning(request=request , message=f'password or username not corret')
    return render(request,'login_view.html')

def dashbaord(request):
    return render(request,'dashbaord.html')

def logout_view(request):
    logout(request=request)
    messages.success(request=request,message='You are logout successfylly')
    return redirect('login_view')
