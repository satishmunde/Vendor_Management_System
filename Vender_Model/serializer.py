from rest_framework import serializers

from .models import Vendor
class VendorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vendor
        fields = '__all__'

        # exclude = [fields,]
        
class AddVenderAPI(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ['vendor_code','name','contact_details','address']
        
        
