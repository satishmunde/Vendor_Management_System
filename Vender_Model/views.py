from django.http import HttpResponse
from django.shortcuts import render,redirect

from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth.hashers import make_password, check_password
from Vender_Model.models import Vendor
from rest_framework.decorators import api_view
from rest_framework.response import Response
from Vender_Model.serializer import VendorSerializer
import json


@api_view(['GET','POST'])
def profile(request):
    vendor =  Vendor.objects.all()
    serializer = VendorSerializer(vendor,many = True)
    if request.method == "GET":
        req = request.GET.get("request")

        if req == "delete":
            id = request.GET.get("vendor_code")
            vendor = Vendor.objects.get(vendor_code = id)
            vendor.delete()
            vendor.save()
            print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")


    # if request.method == 'GET':
    #     vendor =  Vendor.objects.all()
    #     serializer = VendorSerializer(vendor,many = True)

    #     # return Response(serializer.data)
    # elif request.method == 'POST':
    #     data = request.data
    #     serializer = VendorSerializer(data = data)

    #     if serializer.is_valid():
    #         serializer.save()
    #         print(serializer.data)
    #         return Response(serializer.data)
    #     print(serializer.data)
    #     return Response(serializer.errors)
    return render(request,'VP/index.html',{"vendordtls":serializer.data})


def vendor_reg(request):
    return render(request,'VP/index.html')


def get_user(request):
    return render(request,'VP/index.html')


def user_dtl(request):
    return render(request,'VP/index.html')

def delete_user(request):
    return render(request,'VP/index.html') 