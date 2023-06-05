from django.shortcuts import render,redirect
from django.contrib import auth,messages

def home(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('emp_detail:index')
        else:
            messages.info(request,"Credentials Invalid")
            return render(request,'home.html')
    else:
        return render(request,'home.html')
