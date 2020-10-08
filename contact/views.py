from django.shortcuts import render
from django.contrib import messages
from .models import contact
# Create your views here.
def contactus(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')

        contactData=contact(name=name,email=email,subject=subject,message=message)
        contactData.save()
        messages.success(request, 'Message Sent Successfully. We will contact you soon!')

        # or you can use this also
        
        # contactData=contact()
        # contactData.name=request.POST.get('name')
        # contactData.email=request.POST.get('email')

        # contactData.save()
        
    return render(request,'contact.html')
