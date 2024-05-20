from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.contrib.auth.hashers import make_password
# Create your views here.

def index(request):
    return render(request,"index.html")

def signup(request):
    return render(request,"signup.html")

def login(request):
    return render(request,"adminlogin.html")

def doctor(request):
    return render(request,"doctor.html")

def patient(request):
    return render(request,"patient.html")



