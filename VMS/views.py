from django.http import HttpResponse
from django.shortcuts import render,redirect

from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth.hashers import make_password, check_password

def home(request):
    return render(request,'index.html')


