from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
# Create your views here.


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
