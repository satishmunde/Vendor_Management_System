from django.http import HttpResponse
from django.shortcuts import render,redirect

from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth.hashers import make_password, check_password
from Vender_Model.models import Vendor
from rest_framework.decorators import api_view
from rest_framework.response import Response
from Vender_Model.serializer import *
from rest_framework import status
import json


@api_view(['GET','POST'])
def vendor_reg(request):
    print("function called")
    if request.method=='POST':
        print("this is post method")
        serializer = AddVenderAPI(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
        print(serializer.data)
        return Response(serializer.data)
    
    
@api_view(['GET'])
def all_vendor(request):
    
    if request.method == 'GET':
        vendor =  Vendor.objects.all()
        serializer = VendorSerializer(vendor,many = True)

        return Response(serializer.data)
    
    
@api_view(['GET'])
        
def get_vendor(request,vendor_code):
    print(vendor_code)

    try:
        vendor = Vendor.objects.get(vendor_code=vendor_code)
        serializer = VendorSerializer(vendor)
        return Response(serializer.data)
    except Vendor.DoesNotExist:
        return Response(status=404)

        
@api_view(['PUT'])
def update_vendor(request, vendor_id):
    try:
        vendor = Vendor.objects.get(pk=vendor_id)
    except Vendor.DoesNotExist:
        return Response({"error": "Vendor not found"}, status=404)

    serializer = VendorUpdateSerializer(vendor, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    
    return Response(serializer.errors, status=400)
        
    
@api_view(['DELETE'])
def delete_vendor(request, vendor_id):
    try:
        vendor = Vendor.objects.get(pk=vendor_id)
    except Vendor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        vendor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
