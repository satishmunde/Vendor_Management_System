from django.http import HttpResponse
from django.shortcuts import render,redirect

from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth.hashers import make_password, check_password

def home(request):
    return render(request,'index.html')


def vendor_profile(request):
    return render(request,'vendor_profile.html')


def purchace_order(request):
    return render(request,'purchase_order.html')


def performance_evaluation(request):
    return render(request,'performance_evaluation.html')


def logoutUser(request):

    logout(request)
    return redirect('/login')