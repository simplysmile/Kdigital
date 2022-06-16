from django.shortcuts import render

def exboard(request):
    return render(request,'infoTable.html')

def exwrite(request):
    return render(request,'boardWrite.html')