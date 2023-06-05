# Create your views here.
from django.shortcuts import render,redirect
from .models import Detail
from datetime import datetime
import qrcode
from PIL import Image
from django.core.files.base import ContentFile
from io import BytesIO
import base64
from django.contrib import auth



# Create your views here.
def index(request):
    return render(request,'emp/index.html')


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
        prod.telephone_number=int(request.POST["telephone"])
        prod.fax_number=int(request.POST["printer"])
        prod.email_id=request.POST["email"]
        prod.social_media1=request.POST["website1"]
        prod.social_media2=request.POST["website2"]
        prod.address=request.POST["address"]
        prod.role_id=int(request.POST["role"])
        prod.account_created=datetime.now()
        if len(request.FILES) != 0: 
            prod.image_upload=request.FILES['image']

            logo = Image.open(request.FILES['image'])
            basewidth = 85

            wpercent = basewidth / float(logo.size[0])
            hsize = int(float(logo.size[1]) * float(wpercent))
            logo = logo.resize((basewidth, hsize), Image.ANTIALIAS)

            qr_big = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=4)
            qr_big.add_data(request.POST["website1"])
            qr_big.make(fit=True)

            img_qr_big = qr_big.make_image(fill_color="blue", back_color="white").convert("RGB")
            qr_width, qr_height = img_qr_big.size

            logo_width, logo_height = logo.size
            logo_size = min(qr_width, qr_height) // 4

            logo_resized = logo.resize((logo_size, logo_size), Image.ANTIALIAS)
            logo_pos = ((qr_width - logo_size) // 2, (qr_height - logo_size) // 2)
            img_qr_big.paste(logo_resized, logo_pos)

            name=request.POST["firstname"]
            qr_code_buffer=BytesIO()
            img_qr_big.save(qr_code_buffer, format='PNG')
            qr_code_file = ContentFile(qr_code_buffer.getvalue())
            prod.qr_code.save(f"{name}.png", qr_code_file)
         
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

def logout(request):
    auth.logout(request)
    return redirect('home')