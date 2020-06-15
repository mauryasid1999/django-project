from django.shortcuts import render,redirect
from django.core.mail import send_mail
from .models import fbpage

def index(request):
    forms=fbpage.objects.all()


    if request.method=="POST":
        if "sub" in request.POST:
            first_name=request.POST["fm"]
            last_name=request.POST["lm"]
            mobile=request.POST["mobile"]
            password=request.POST['newpass']
            dateof_birth=request.POST['dob']
            gender=request.POST['fuvk']
      
            forms1=fbpage( first_name= first_name,last_name=last_name,mobile=mobile,password=password,dateof_birth=dateof_birth, gender= gender)
            forms1.save()
         
   
            return redirect('/')
    
    return render(request,"index.htm",{"forms":forms})



