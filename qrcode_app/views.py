from django.shortcuts import render



# Create your views here.
def qrcode(request):
    if request.method=="POST":
        param=request.POST['param']
        print(param)
    return render(request,'qrcode/qrcode.html')