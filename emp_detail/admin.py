from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Detail,Roles

# Register your models here.
admin.site.register(Roles)
admin.site.register(Detail)