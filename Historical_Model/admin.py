from django.contrib import admin
from .models import HistoricalPerformance

class HistoricalPerformanceAdmin(admin.ModelAdmin):
    list_display = ('vendor', 'date', 'on_time_delivery_rate', 'quality_rating_avg', 'average_response_time', 'fulfillment_rate')
    search_fields = ['vendor_code', 'date']
    list_filter = ['vendor', 'date']

admin.site.register(HistoricalPerformance, HistoricalPerformanceAdmin)
 