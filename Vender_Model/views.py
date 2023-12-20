from django.http import HttpResponse
from django.shortcuts import render,redirect


from Vender_Model.models import Vendor
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests

import json


@api_view(['GET','POST','PUT'])
def profile(request):
    print('-----------------------'+str(request.method))
    data={}
    url = 'http://127.0.0.1:8000/api/vendors/'
    if request.method == "GET":

        try:
            response = requests.get(url)
            if response.status_code == 200:
                vendors = response.json()
                # Process or use the vendor data here
                data={'allvendor':vendors}
            
            else:
                print(f"Failed to fetch vendors. Status code: {response.status_code}")
        except requests.RequestException as e:
            print(f"Error: {e}")
    
    elif request.method == "POST":
        print("----------------------------------------------")
        req = request.POST.get('req') 
        if req == "add":
            name = request.POST.get('vname')
            contact =  request.POST.get('vcontact')
            address =  request.POST.get('vaddress')
            vendorcode = Vendor.objects.last()
            
            if not vendorcode :
                id = 'VC10000001'
            else:
                id = int(vendorcode.vendor_code[2:])
                id += 1
                id='VC'+str(id)
            vdata = {'vendor_code':id,'name':name,'contact_details':contact,'address':address}
            print(vdata)
            headers = {"Content-Type":"application/json"}
            res=requests.post(url,headers=headers,data=json.dumps(vdata))
        elif req == 'update':
            code = request.POST.get('upvcid')
            updated_data = {
            "vendor_code":code,
            'name': request.POST.get('name'),
            'contact_details': request.POST.get('contact'),
            'address': request.POST.get('address'),
        }

            url = f'http://127.0.0.1:8000/api/vendors/{code}/'
            headers = {"Content-Type": "application/json"}

            try:
                response = requests.put(url, headers=headers, data=json.dumps(updated_data))
                if response.status_code == 200:
                    return Response({'message': 'Vendor updated successfully'})
            except requests.RequestException as e:
                return Response({'error': f'Request Exception: {str(e)}'}, status=500)
     
        
    try:
        
        response = requests.get(url)
        if response.status_code == 200:
            vendors = response.json()
            
            data={'allvendor':vendors}
            
        else:
            print(f"Failed to fetch vendors. Status code: {response.status_code}")
    except requests.RequestException as e:
        print(f"Error: {e}")

    return render(request,'VP/index.html',data)



def user_dtl(request):
    return render(request,'VP/index.html')

