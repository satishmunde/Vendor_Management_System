from django.contrib import admin
from .models import Vendor

class VendorAdmin(admin.ModelAdmin): 
    list_display = ('name', 'vendor_code','contact_details','address', 'on_time_delivery_rate', 'quality_rating_avg','average_response_time','fulfillment_rate')  # Fields to display in the list
    search_fields = ['name', 'vendor_code']  # Enable search by name and vendor code


admin.site.register(Vendor, VendorAdmin)
