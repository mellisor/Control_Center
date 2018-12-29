from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def login_view(request):
    if request.method == "POST":
        if request.POST.get('email'):
            return create_user(request)
        else:
            return login_user(request)
        return redirect('/dashboard/')
    return render(request,'login.html')

def create_user(request):
    # Create Error dictionary
    errors = dict()
    # Check if passwords match
    if request.POST.get('password') != request.POST.get('password_confirm'):
        errors['password'] = True
    if len(User.objects.filter(username=request.POST.get('username'))) > 0:
        errors['user_already_exists'] = True
    if len(errors.keys()) > 0:
        return render(request,'login.html',context=errors)
    u = User.objects.create_user(username=request.POST.get('username'),password=request.POST.get('password'),email=request.POST.get('email'))
    u.save()
    return login_user(request)

def login_user(request):
    uname = request.POST.get('username')
    pwd = request.POST.get('password')
    user = authenticate(username=uname,password=pwd)
    if user:
        login(request,user)
        return redirect('/dashboard/')
    return render(request,'login.html',context={'user_does_not_exist':True})

def logout_view(request):
    logout(request)
    return redirect('/accounts/login/')