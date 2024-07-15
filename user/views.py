from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as authlogin,logout as authlogout

# Create your views here.
def signup(request):
    user=None
    error_message=0
    if request.POST:
       username=request.POST.get('username')
       password=request.POST.get('password')
       try:
         user=User.objects.create_user(username=username,password=password)  
       except Exception as e:
            error_message=str(e)      
    return render(request,'users/create.html',{'user':user,'error_message':error_message})

def login(request):
    if request.POST:
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user:
            authlogin(request,user)
            return redirect('list')
        else:
            print("error")    
    return render(request,'users/login.html')

def logout(request):
    authlogout(request)
    return redirect('login')