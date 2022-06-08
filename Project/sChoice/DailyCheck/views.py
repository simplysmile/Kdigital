from django.shortcuts import render

# Create your views here.

def calendar(request):
    return render(request,'calendar.html')

def mealCheck(request):
    return render(request,'mealCheck.html')
def exerciseCheck(request):
    return render(request,'exerciseCheck.html')