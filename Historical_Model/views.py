from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import render, redirect
from datetime import timedelta
from api.serializer import *




# from .models import PurchaseOrder
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
import random

import json
from django.db.models import Avg 
# Create your views here.


def evaluate(request,vendor_id):
    data={}
    req = request.POST.get('req')
    url = "http://127.0.0.1:8000/api/po/"


    

    if request.method == 'POST':
        if req == 'update':
            poid = request.POST.get("poid")
            status = request.POST.get('postatus')
            ordDate  = timezone.now()
                        
            if status == "delevered":
                 # Using UTC time for consistency
                po = {
                    "po_number": poid,
                    "vendor":vendor_id,
                    "delivery_date": str(timezone.now()),
                    "quality_rating": str(random.randint(1, 10)),
                    "status": status,
                }
                calculate_performance_metrics(vendor_id)
                # update_metrics_on_time_delivery(poid)
            elif status == "in-transist":
                 # Using UTC time for consistency
                po = {
                    "po_number": poid,
                    "vendor":vendor_id,
                    "acknowledgment_date": str(timezone.now()),
                    "status": status,
                }
            else:
                po = {
                    "po_number": poid,
                    "vendor":vendor_id,
                    "status": status,
                    "delivery_date": "",
                }

            # Make sure to handle appropriate error cases here, this is a basic example
            try:
                print(po)
                headers = {"Content-Type": "application/json"}
                res = requests.put(url + str(poid) + '/', headers=headers, data=json.dumps(po))

                if res.status_code == 200:  # Assuming a successful update returns status code 200
                    print("Update Successful")
                else:
                    print("Update Failed with status code:", res.status_code)
                    print("Response Content:", res.content)
            except requests.RequestException as e:
                print("Request Exception:", e)
    purchase_orders = PurchaseOrder.objects.filter(vendor=vendor_id).exclude(status='delevered')


    serializer = POSerializer(purchase_orders, many=True)
    
    
    data.update({"allpo": serializer.data})
    
    perurl = f" http://127.0.0.1:8000/api/performance/{vendor_id}/"
    res =  requests.get(perurl)
    data.update({"mat": res.json()})
    print(res.json)
    return render(request,"PE/performance_evaluation.html",data)


from django.db.models import Count, Avg



from django.db.models import Avg

from django.utils import timezone   





def calculate_performance_metrics(vendor):
    # On-Time Delivery Rate
    delevered_pos = PurchaseOrder.objects.filter(vendor=vendor, status='delevered')
    total_delevered_pos = delevered_pos.count()

    on_time_delivery = delevered_pos.filter(delivery_date__lte=str(timezone.now())).count()

    on_time_delivery_rate = (on_time_delivery / total_delevered_pos) * 100 if total_delevered_pos > 0 else 0.0

    delivered_pos_with_rating = PurchaseOrder.objects.filter(vendor=vendor, quality_rating__isnull=False, status='delevered')
    print(delivered_pos_with_rating)

    quality_rating_avg = delivered_pos_with_rating.aggregate(quality_avg=Avg('quality_rating')).get('quality_avg') or 0.0
    print(quality_rating_avg)
    # Average Response Time
    acknowledged_pos = PurchaseOrder.objects.filter(vendor=vendor, acknowledgment_date__isnull=False)
    response_times = [(ack_po.acknowledgment_date - ack_po.issue_date).total_seconds() / 3600 for ack_po in acknowledged_pos]
    average_response_time = sum(response_times) / len(response_times) if response_times else 0.0

    total_pos = PurchaseOrder.objects.filter(vendor=vendor)

    fulfilled_pos = total_pos.filter(status='delevered').count()

    fulfillment_rate = (fulfilled_pos / total_pos.count()) * 100 if total_pos.count() > 0 else 0.0
 
    # Create Historical Performance record
    vendor_ins =Vendor.objects.get(vendor_code = vendor),
    HistoricalPerformance.objects.create(
        vendor=Vendor.objects.get(vendor_code = vendor),
        date=timezone.now(),
        on_time_delivery_rate=on_time_delivery_rate,
        quality_rating_avg=quality_rating_avg,
        average_response_time=average_response_time,
        fulfillment_rate=fulfillment_rate
    )

    all_orders_metrics = HistoricalPerformance.objects.filter(vendor=vendor)
    aggregated_metrics = all_orders_metrics.aggregate(
        avg_on_time=Avg('on_time_delivery_rate'),
        avg_quality=Avg('quality_rating_avg'),
        avg_response=Avg('average_response_time'),
        avg_fulfillment=Avg('fulfillment_rate')
    )

    Vendor.objects.filter(pk=vendor).update(
        on_time_delivery_rate=aggregated_metrics['avg_on_time'],
        quality_rating_avg= aggregated_metrics['avg_quality'],
        average_response_time= aggregated_metrics['avg_response'],
        fulfillment_rate= aggregated_metrics['avg_fulfillment']
    )