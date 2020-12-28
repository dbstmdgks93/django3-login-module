from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from .forms import SignUpForm
from .models import CustomUser
from django.contrib.auth import login, logout, authenticate

# Create your views here.
def home(request):
    return render(request, 'mainpage/home.html')

# def signup(request):
#     return render(request, 'mainpage/signup.html',{'form':SignUpForm()})

def signup(request):
    if request.method =='GET':
        return render(request, 'mainpage/signup.html',{'form':SignUpForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = CustomUser.objects.create_user(\
                    request.POST['username'],\
                    password=request.POST['password1'],\
                    name=request.POST['name'],\
                    birth=request.POST['birth'],\
                    gender=request.POST['gender'])
                user.save()
                return redirect('home')
            except IntegrityError:
                return render(request,'mainpage/signup.html',{'form':SignUpForm()})
        else:
            return render(request,'mainpage/signup.html',{'form':SignUpForm()})

def loginuser(request):
    if request.method == 'GET':
        return render(request, 'mainpage/loginuser.html',{'form':AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'mainpage/loginuser.html',{'form':AuthenticationForm(),'error':'Username and password is not match'})
        else:
            # login
            login(request, user)
            return redirect('home')

def logoutuser(request):
    if request.method=='POST':
        logout(request)
        return redirect('home')