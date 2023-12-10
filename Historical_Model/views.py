from django.shortcuts import render

# Create your views here.


def evaluate(request):
    return render(request,"PE/performance_evaluation.html")