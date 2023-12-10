from Vender_Model.views import *
from Purchase_Order_Model.views import *

from django.urls import path, include


urlpatterns = [
    path('index/', profile),
]
