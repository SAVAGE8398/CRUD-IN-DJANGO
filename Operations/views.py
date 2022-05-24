from django.shortcuts import render, redirect
from .models import User

# Create your views here.
def index(request):
    if request.method == 'POST':
        data=User(FirstNameF=request.POST["txtfname"],LastNameF=request.POST["txtlname"],EmailF=request.POST["txtemail"],PasswordF=request.POST["txtpassword"])
        data.save()
    return render(request,'index.html')
def operations(request):
    data=User.objects.all()
    return render(request,'operations.html',{"data":data})
def editrecord(request):     
    s=User.objects.get(pk=request.GET["f"])    
    return render(request,"editrecord.html",{'res':s})
def edit(request):           #code to update record from database to contact table
    a=request.POST["txtfname"]
    b=request.POST["txtlname"]
    c=request.POST["txtemail"]
    d=request.POST["txtpassword"]
    s = User.objects.get(pk=request.POST["txtid"])
    s.FirstNameF=a
    s.LastNameF=b
    s.EmailF=c
    s.PasswordF=d
    s.save()
    return redirect('operations')
def deleterecord(request):
    s=User.objects.get(pk=request.GET["f"])
    s.delete()
    return redirect('operations')

