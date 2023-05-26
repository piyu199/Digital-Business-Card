from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,HttpResponse
from .models import Detail
from datetime import datetime


# Create your views here.
def home(request):
    return render(request,'home.html')


def list_details(request):
    business_cards = Detail.objects.all()
    #current_image = f"{MEDIA_ROOT}images\{business_cards.image_upload}"
    print("\n \n \n ")
    #print(current_image)
    context={
        'business_cards':business_cards
    }
    return render(request,"list_details.html",context)


def add_emp(request):
    if request.method=="POST":
        prod=Detail()
        prod.first_name=request.POST["firstname"]
        prod.last_name=request.POST["lastname"]
        prod.phone=int(request.POST["phone"])
        prod.account_created=datetime.now()
        if len(request.FILES) != 0:
            prod.image_upload=request.FILES['image']
        
        prod.save()
        return HttpResponse("Employee added Successfully")
    elif request.method=='GET':
        return render(request,'add_details.html')
    else:
        return HttpResponse("An Exception Occured!Employee has not been Added")
    

def display_card(request,id=0):
    if id:
        try:
            emp_details=Detail.objects.get(id=id)
            context={
                'emp_details':emp_details
            }
            return render(request,'display_card.html',context)
        except:
            return HttpResponse("Somethong Went wrong")

    return render(request,'display_card.html')