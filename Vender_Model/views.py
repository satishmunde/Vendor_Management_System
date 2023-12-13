from django.http import HttpResponse
from django.shortcuts import render,redirect

from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth.hashers import make_password, check_password
from Vender_Model.models import Vendor
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
from Vender_Model.serializer import *
import json


@api_view(['GET','POST'])
def profile(request):
    
    url = 'http://127.0.0.1:8000/vendor-dtl/api/allVendor'  
    response = requests.get(url, headers={'Content-Type': 'application/json'})
    if response.status_code == 200:
    
        updated_vendor = response.json()
        data = { "allvendor":updated_vendor}

    else:
        print("Failed to update vendor. Status code:", response.status_code)
    
 
    return render(request,'VP/index.html',data)

@api_view(['GET','POST'])
def vendor_reg(request):
    print("function called")
    if request.method=='POST':
       name =  request.POST.get('vname')
       contact_details =  request.POST.get('vcontact')
       address = request.POST.get('vaddress')
       id  = Vendor.objects.last()
       if id.vendor_code == "":
           
            vendor_code = "VC100000001"
       else:
            vender_code = id.vendor_code[2:]
            vender_code += 1
            vender_code ="VC"+str(vender_code)
    data = json.dumps(vendor_code,name,contact_details,address)
    response = requests.get('http://127.0.0.1:8000/vendor-dtl/api/addVendor/',data)
    if response.status_code == 200:
        data = response.json()  # Convert the JSON response to Python data
    else:
        data = [] 
        
    print(data)
        
    
    # return render(request,'VP/index.html')


def get_user(request):
    return render(request,'VP/index.html')


def user_dtl(request):
    return render(request,'VP/index.html')

def delete_user(request):
    return render(request,'VP/index.html') 