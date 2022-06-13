from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

def calendar(request):
    return render(request,'calendar.html')

def mealCheck(request):
    return render(request,'mealCheck.html')


def exerciseCheck(request):
    return render(request,'exerciseCheck.html')

def exercise1(request):
    return JsonResponse()


def myStatus(request):
    return render(request,'myStatus.html')
def selfCheck(request):
    return render(request,'selfCheck.html')