from django.shortcuts import render

# Create your views here.

def purchase_order(request):
    return render(request, 'PO/index.html')

def get_ord(request):
    return render(request, 'PO/index.html')

def get_all_ord(request):
    return render(request, 'PO/index.html')

def gen_ord(request):
    return render(request, 'PO/index.html')

def update_ord(request):
    return render(request, 'PO/index.html')