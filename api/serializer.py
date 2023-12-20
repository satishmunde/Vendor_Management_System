from rest_framework import serializers
from Vender_Model.models import *
from Purchase_Order_Model.models import *
from Historical_Model.models import HistoricalPerformance # Import your VendorPerformance model

class VendorPerformanceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'

class VendorSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Vendor
        fields = ['vendor_code','name','contact_details','address']
        
        
class POSerializer(serializers.HyperlinkedModelSerializer):
    vendor = serializers.PrimaryKeyRelatedField(queryset=Vendor.objects.all())

    class Meta:
        model = PurchaseOrder
        fields = ['po_number','vendor','order_date','items','quantity','delivery_date','issue_date','status','acknowledgment_date','quality_rating'] 