from rest_framework import serializers
from Vender_Model.models import *
from Purchase_Order_Model.models import *

class VendorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vendor
        fields = ['vendor_code','name','contact_details','address']
        
        
class POSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = ['po_number','vendor','order_date','items','quantity','delivery_date','issue_date']