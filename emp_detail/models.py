
from django.db import models
from datetime import datetime

# Create your models here.


class Roles(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class Detail(models.Model):
    first_name=models.CharField(max_length=100,null=True)
    last_name=models.CharField(max_length=100,null=True)
    phone = models.IntegerField(default=0)
    telephone_number=models.IntegerField(default=0)
    fax_number=models.IntegerField(default=0)
    email_id=models.EmailField()
    account_created=models.DateField(default=datetime.now)
    image_upload=models.ImageField(upload_to='images',null=True)
    qr_code=models.ImageField(upload_to='qrcode',null=True)
    social_media1=models.CharField(max_length=100,null=True)
    social_media2=models.CharField(max_length=100,null=True)
    address = models.CharField(max_length=200,null=True)
    role=models.ForeignKey(Roles,on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s %s" % (self.first_name, self.last_name,self.email_id)

