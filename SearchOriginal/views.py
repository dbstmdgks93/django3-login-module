from django.shortcuts import render, redirect

# Create your views here.

def home(request):
    cur_user = request.user
    if cur_user.is_authenticated:
        return render(request,'SearchOriginal/home.html')
    else:
        return redirect('home')