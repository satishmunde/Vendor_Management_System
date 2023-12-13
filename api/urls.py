from Vender_Model.views import *

from django.urls import path, include
from .views import *
# import api.views

urlpatterns = [

    path('addVendor/',vendor_reg),
    path('allVendor/',all_vendor),
    path('getVendor/<vendor_code>/',get_vendor),
    path('updateVendor/',update_vendor),
    path('deleteVendor/<vendor_id>/',delete_vendor),
]
