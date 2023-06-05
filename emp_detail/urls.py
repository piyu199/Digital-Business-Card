from django.urls import path
from . import views
from django.conf import settings  
from django.conf.urls.static import static 

app_name="emp_detail"

urlpatterns = [
    path('',views.index,name='index'),
    path('list_details',views.list_details,name='list_details'),
    path('add_emp',views.add_emp,name='add_emp'),
    path('display_card',views.display_card,name='display_card'),
    path('display_card/<int:id>',views.display_card,name='display_card'),
    path('logout',views.logout,name='logout'),
]
if settings.DEBUG:  
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)