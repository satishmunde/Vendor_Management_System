from django.db import models

class Vendor(models.Model):
    vendor_code = models.CharField(max_length=50, unique=True, primary_key=True)
    name = models.CharField(max_length=100)
    contact_details = models.TextField()
    address = models.TextField()  
    on_time_delivery_rate = models.FloatField(default=0.0)
    quality_rating_avg = models.FloatField(default=0.0)
    average_response_time = models.FloatField(default=0.0)
    fulfillment_rate = models.FloatField(default=0.0)

    def __str__(self):
        return self.vendor_code
  