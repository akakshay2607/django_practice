from django.http import HttpResponse
from django.shortcuts import render

def aboutUs(request):
    return HttpResponse('Welcome to Pyra')

def home(request):
    return render(request,'index.html')

def services(reqquest):
    return HttpResponse("<b>Services</b>")

def service(request,courseid):
    return HttpResponse(courseid)