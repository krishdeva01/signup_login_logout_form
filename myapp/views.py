from django.shortcuts import  render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.db import IntegrityError
from . models import Log

def register(request):
    if request.method == 'GET':
        return render(request,'register.html',{'form':UserCreationForm()})
    else:
        
        if request.POST.get('password1') == request.POST.get('password2'):
            try:
                user = User.objects.create_user(request.POST.get('username'),password = request.POST.get('password1'))
                user.save()
                login(request,user)
                return render(request,'home.html')
            except ValueError:
                return render(request,'home.html')
            except IntegrityError:
                return render(request,'register.html',{'error':'The username you entered is Already taken!!!'})
      
        else:
            return render(request,'register.html',{'error':'The password you are entered is incorrect...Please Try Again'})

def log(request):
    logs = Log.objects.all()
    return render(request,'registration/log.html',{'logs':logs})