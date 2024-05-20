from django.urls import path
from django.conf import settings
from .views import *
from django.conf.urls.static import static

urlpatterns = [
    path("",index),
    path("signup/",signup),
    path("adminlogin/",login),
    path("doctor/",doctor),
    path("patient/",patient),
    
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

 