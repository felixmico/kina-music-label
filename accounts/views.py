import json

from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse, HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib.auth import get_user_model
User = get_user_model
from .models import User as artistsUser
from django.contrib import auth




def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1==password2:
            if artistsUser.objects.filter(username=username).exists():
                print('Username Taken')
                
            elif artistsUser.objects.filter(email=email).exists():

                print('Email Taken')   
            else:
                user = artistsUser.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save();
                print('Registration confirm')
                return redirect('login')
        
        else:

            print('password not matching')



        return redirect('/')
         
    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        artistsUser = auth.authenticate(email=email, password=password)
        if artistsUser is not None:
            auth.login(request, artistsUser)
            return redirect('/')
        else:
            print('invalid credential')
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')            

def logout_user(request):
    logout(request)
    return redirect('core:home')

