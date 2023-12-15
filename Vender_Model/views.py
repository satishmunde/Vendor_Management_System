from django.http import HttpResponse
from django.shortcuts import render,redirect


from Vender_Model.models import Vendor
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests

import json


@api_view(['GET','POST'])
def profile(request):
    
    # url = 'http://127.0.0.1:8000/vendor-dtl/api/allVendor'  
    # response = requests.get(url, headers={'Content-Type': 'application/json'})
    # if response.status_code == 200:
    
    #     updated_vendor = response.json()
    #     data = { "allvendor":updated_vendor}

    # else:
    #     print("Failed to update vendor. Status code:", response.status_code)
    
 
    return render(request,'VP/index.html')

# @api_view(['GET','POST'])
# def vendor_reg(request):
#     if request.method == 'POST':
#         name = request.POST.get('vname')
#         contact_details = request.POST.get('vcontact')
#         address = request.POST.get('vaddress')
        
#         id = Vendor.objects.last()
#         if id.vendor_code == "":
#             vendor_code = "VC100000001"
#         else:
#             vendor_code = int(id.vendor_code[2:])
#             vendor_code += 1
#             vendor_code = "VC" + str(vendor_code)

#         json_string = "{'vendor_code': '" + vendor_code + "', 'name': '" + name + "', 'contact_details': '" + contact_details + "', 'address': '" + address + "'}"

        
#         # data = {
#         #     'vendor_code': vendor_code,
#         #     'name': name,
#         #     'contact_details': contact_details,
#         #     'address': address
#         # }
        
#         headers = {
#             "Content-Type": "application/json",
#             # Add any other headers if needed
            
#         }
#         jdata = json.dumps(json_string)
#         # print(jdata)
#         try:
#             response = requests.post('http://127.0.0.1:8000/vendor-dtl/api/addVendor/', data=json_string)
#             response.raise_for_status()  # Raise an error for 4XX or 5XX status codes
            
#             if response.status_code == 200:
#                 data = response.json()  # Convert the JSON response to Python data
#             else:
#                 data = []  # Define what should happen on unsuccessful requests
#         except requests.RequestException as e:
#             print("Request Error:", e)
#             data = []  # Handle the case where the request encounters an error
            
#         print(data)  # Print or handle the response data as needed

    
#     # return render(request,'VP/index.html')


# def get_user(request):
#     return render(request,'VP/index.html')


# def user_dtl(request):
#     return render(request,'VP/index.html')

# def delete_user(request):
#     return render(request,'VP/index.html') 