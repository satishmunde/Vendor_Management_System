from django.db import models
from Vender_Model.models import *


class PurchaseOrder(models.Model):
    STATUS_CHOICES = (
        ('ordered', 'Ordered'),
        ('in-transist', 'In-Transist'),
        ('delevered', 'Delevered'),
        ('canceled', 'Canceled'), 
    )

    po_number = models.CharField(max_length=50, unique=True ,primary_key=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    quality_rating = models.FloatField(null=True, blank=True)
    issue_date = models.DateTimeField()
    acknowledgment_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"PO: {self.po_number} - Vendor: {self.vendor.vendor_code}"
 