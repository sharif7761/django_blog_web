from django.shortcuts import render

from .models import about
from .models import slider
from .models import client

def home(request):
    aboutData=about.objects.all()[0]
    sliderData=slider.objects.all()
    clientData=client.objects.all()
    context={
        'about':aboutData,
        'slider':sliderData,
        'client':clientData
    }
    return render(request,'index.html',context)

def aboutus(request):
    return render(request,'about.html')


