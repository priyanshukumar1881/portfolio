from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request,"index.html")


def aboutUs(request):
    return render(request,"about.html")

def contactUs(request):
    return render(request,"contact.html")

def project(request):
    return render(request,"project.html")

def service(request):
    return render(request,"service.html")
    
def gallary(request):
    return render(request,"gallary.html")

def socalmedia(request):
    return render(request,"socalmedia.html")

def workexperience(request):
    return render(request,"workexp.html")