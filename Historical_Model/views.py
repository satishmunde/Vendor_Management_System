from django.shortcuts import render

# Create your views here.


def evaluate(request):
    return render(request,"performance_evaluation.html")