from rest_framework import viewsets
from Vender_Model.models import Vendor 
from Purchase_Order_Model.models import PurchaseOrder
from api.serializer import VendorSerializer,POSerializer,VendorPerformanceSerializer
from Historical_Model.models import HistoricalPerformance 
class VendorPerformanceViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorPerformanceSerializer
    lookup_field = 'pk'

class VendorViewSet(viewsets.ModelViewSet): 
    
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    lookup_field = 'pk'
    # Other configurations or methods if needed


class POViewSet(viewsets.ModelViewSet): 
    lookup_field = 'pk'
    queryset = PurchaseOrder.objects.all()
    serializer_class = POSerializer
    # Other configurations or methods if needed
