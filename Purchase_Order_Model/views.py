from django.shortcuts import render

# Create your views here.

def purchase_order(request):
    return render(request, 'PO/purchase_order.html')