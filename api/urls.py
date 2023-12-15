from django.urls import path, include
from rest_framework import routers
from api.views import *  # Assuming Vendor is your viewset

router = routers.DefaultRouter()
router.register(r'vendors', VendorViewSet)
router.register(r'po', POViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # Other URL patterns
]
