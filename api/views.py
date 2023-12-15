from rest_framework import viewsets
from Vender_Model.models import Vendor 
from Purchase_Order_Model.models import PurchaseOrder
from api.serializer import VendorSerializer,POSerializer  # Assuming VendorSerializer is your serializer

class VendorViewSet(viewsets.ModelViewSet):  # Use viewsets.ModelViewSet or appropriate
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    # Other configurations or methods if needed


class POViewSet(viewsets.ModelViewSet):  # Use viewsets.ModelViewSet or appropriate
    queryset = PurchaseOrder.objects.all()
    serializer_class = POSerializer
    # Other configurations or methods if needed
