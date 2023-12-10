from django.contrib import admin
from .models import PurchaseOrder

class PurchaseOrderAdmin(admin.ModelAdmin):
    list_display = ('po_number', 'vendor', 'order_date', 'delivery_date','items','quantity','status','quality_rating','issue_date','acknowledgment_date')  # Fields to display in the list
    search_fields = ['po_number', 'vendor__name']  # Enable search by PO number and vendor name
    list_filter = ['status', 'order_date', 'delivery_date']  # Add filters by status, order date, and delivery date

admin.site.register(PurchaseOrder, PurchaseOrderAdmin) 
