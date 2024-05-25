from django.urls import path
from django.conf import settings
from .views import *
from django.conf.urls.static import static

urlpatterns = [
    path("",index),
    path("signup/",signup),
    path("adminsignup/",admin_signup),
    path("login/",login),
    path("admin_login/",admin_login),
    path("doctor/",doctor),
    path("doctor_signup/",doctor_signup),
    path("patient/",patient),
    path("patient_data/",patient_data),
    path("patientview/",patientview),
    path("delete/<int:pk>/",delete_patient,name='delete'),
    path("doctorlogin/",doctorlogin),
    path("doctor_login/",doctor_login),
    path("doctorview/",doctorview),
    path("deletedoctor/<int:pk>/",delete_doctor,name='deletedoctor'),
    
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

 