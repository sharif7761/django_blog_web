from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def employee(request):
    return HttpResponse("employee home page")

def profile(request):
    return render(request,'employee/profile.html')
