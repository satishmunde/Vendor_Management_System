from django.http import HttpResponse
from django.shortcuts import render, redirect
from datetime import datetime,timedelta
from api.serializer import *


from .models import PurchaseOrder
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
from django.utils import timezone   

import json


def purchase_order(request):
    print("-----------------------" + str(request.method))
    data = {}
    url = "http://127.0.0.1:8000/api/po/"

    if request.method == "POST":
        req = request.POST.get("req")
        print("----------------------------------------------",req)
        
        if req == "add":
            vendor = request.POST.get("vendor_id")
        
            item = request.POST.get("items")
            qty = request.POST.get("quantity")

       
            dDate = timezone.now()+timedelta(days=5)
            print(dDate)
            
       
            ordDate = timezone.now()
            



        
            purchaseCode = PurchaseOrder.objects.last()
            

            if not purchaseCode:
                id = "PO10000001"
            else:
                id = int(purchaseCode.po_number[2:])
                id += 1
                id = "PO" + str(id)
            po = {
                "po_number": id,
                "vendor": vendor,
                "order_date": str(ordDate),
                "delivery_date":str(dDate) ,
                "issue_date":str(ordDate),
                "items": [
                    {
                        "item_name": item,
                        "item_code": "A001",
                    
                    },
                    
                ],
                "quantity":qty ,
                "status": "ordered",
            } 

            print(po)
            print(json.dumps(po))
            headers = {"Content-Type": "application/json"}
            res = requests.post(url, headers=headers, data=json.dumps(po))
            print(res)

        elif req == 'update':
            vendor = request.POST.get("vendor_id")
        
            item = request.POST.get("items")
            qty = request.POST.get("quantity")
            poid = request.POST.get('poid')

 
            ordDate = timezone.now()
           
            po = {
                "po_number": poid,
                "vendor": vendor,
                "order_date": str(ordDate),

                "issue_date":str(ordDate),
                "items": [
                    {
                        "item_name": item,
                        "item_code": "A001",
                    
                    },
                    
                ],
                "quantity":qty ,
                "status": "ordered",
            } 
            headers = {"Content-Type": "application/json"}
            res = requests.put(url+str(poid)+'/', headers=headers, data=json.dumps(po))
            print(res)
            

    orderby = False
    

    if request.GET.get('vendor_id') and request.GET.get('vendor_id')!=None:
        orderby = True
        
    print("-------------------------                           " +str(orderby))
    if orderby :
        vcode = requests.get("http://127.0.0.1:8000/api/vendors/")
        if vcode.status_code == 200:
            vendors = vcode.json()
        vendor_id = request.GET.get('vendor_id')
        purchase_orders = PurchaseOrder.objects.filter(vendor=vendor_id)  # Filter based on vendor_id

        serializer = POSerializer(purchase_orders, many=True)
        
        print("-------------------------------"+str(serializer.data))
        data = {"allpo": serializer.data, "vendors":vendors}

    else:            
        try:
            vcode = requests.get("http://127.0.0.1:8000/api/vendors/")
            if vcode.status_code == 200:
                vendors = vcode.json()
            response = requests.get(url)
            if response.status_code == 200:
                po = response.json()

                data = {"allpo": po, "vendors":vendors}

            else:
                print(f"Failed to fetch vendors. Status code: {response.status_code}")
        except requests.RequestException as e:
            print(f"Error: {e}")

    return render(request, "PO/index.html", data)
