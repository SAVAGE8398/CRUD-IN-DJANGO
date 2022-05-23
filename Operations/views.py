from django.shortcuts import render
from .models import User

# Create your views here.
def index(request):
    if request.method == 'POST':
        data=User(FirstNameF=request.POST["txtfname"],LastNameF=request.POST["txtlname"],EmailF=request.POST["txtemail"],PasswordF=request.POST["txtpassword"])
        data.save()
    return render(request,'index.html')