from django.http import HttpResponse
from django.shortcuts import render, redirect
from datetime import datetime,timedelta


from .models import PurchaseOrder
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests

import json


def purchase_order(request):
    print("-----------------------" + str(request.method))
    data = {}
    url = "http://127.0.0.1:8000/api/po/"

    if request.method == "POST":
        print("----------------------------------------------")
        req = request.POST.get("req")
        if req == "add":
            vendor = request.POST.get("vendor_id")
        
            item = request.POST.get("items")
            qty = request.POST.get("quantity")
            dDate = datetime.now().date()+ timedelta(days=5)
            ordDate = datetime.now()
        
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
    try:
        response = requests.get(url)
        if response.status_code == 200:
            po = response.json()

            data = {"allpo": po}

        else:
            print(f"Failed to fetch vendors. Status code: {response.status_code}")
    except requests.RequestException as e:
        print(f"Error: {e}")

    return render(request, "PO/index.html", data)
