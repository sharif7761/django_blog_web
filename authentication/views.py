from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from employee.views import employee

# Create your views here.
def authlogin(request):
    if(request.method=='POST'):
        name=request.POST['name']
        password=request.POST['password']
        user=authenticate(request,username=name,password=password)
        if user is not None:
            login(request,user)
            return redirect("employee_profile")
        else:   
            messages.error(request, 'Your Username or Password is incorrect!') 
    return render(request,'authentication/login.html')

def authregistration(request):
    if(request.method=="POST"):
        username=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']

        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists')
            else:    
                user=User.objects.create_user(username=username,password=password,email=email)
                user.save()
                messages.success(request, 'Registration successful! Please login') 
                return redirect('login')    
        else:   
            messages.error(request, 'Confirm password does not match')     


    return render(request,'authentication/registration.html')

def forgotPassword(request):
    return render(request,'authentication/forget.html')  

def userlogout(request):
    logout(request)
    return redirect('login')              