from django.urls import path
from . import views

app_name='qrcode'

urlpatterns = [
    path('',views.qrcode,name='qrcode'),
]