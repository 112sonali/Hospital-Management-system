from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.contrib.auth.hashers import make_password , check_password
# Create your views here.

def index(request):
    return render(request,"index.html")

def signup(request):
    return render(request,"signup.html")

def admin_signup(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobileno = request.POST.get('mobileno')
        password = make_password(request.POST.get('password'))
        if AdminSignup.objects.filter(email=email).exists():
            messages.error(request,"Email Already Exists")
            return redirect("/")
        else:
            AdminSignup.objects.create(name=name, email=email, mobileno=mobileno,
                                  password=password)
            return redirect("/login/")


def login(request):
    return render(request,"adminlogin.html")

def admin_login(request):
    if request.method == "POST":
        login = AdminSignup.objects.get(email = request.POST['email'])
        if check_password(request.POST['password'],login.password):
            request.session['login'] = True
            request.session['email'] = login.email
            return redirect('/doctorview/')
        else:
            messages.error(request,"Invalid Id Password")
            return redirect("/doctor/")
        
def doctor(request):
    return render(request,"doctor.html")

def doctor_signup(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        experience = request.POST.get('experience')
        specialization = request.POST.get('specialization')
        address = request.POST.get('address')
        mobileno = request.POST.get('mobileno')
        password = make_password(request.POST.get('password'))
        degree = request.POST.get('degree')
        image = request.FILES.get('image')
        if Doctor.objects.filter(email=email).exists():
           messages.error(request,"Email Already Exists")
           return redirect("/")
        else:
            Doctor.objects.create(name=name, email=email,gender=gender,dob=dob,
                                   experience=experience,specialization=specialization,
                                   address=address,mobileno=mobileno,password=password,degree=degree,image=image)
            return redirect("/doctorlogin/")
        
#def doctor_login(request):
    #if request.method == "POST":
        #login = Doctor.objects.get(email = request.POST['email'])
        #if check_password(request.POST['password'],login.password):
            #request.session['login'] = True
            #request.session['email'] = login.email
           # return redirect('/patient/')
        #else:
            #messages.error(request,"Invalid Id Password")
            #return redirect("/index/")

def patient(request):
    doctor_obj = Doctor.objects.all()
    patient_obj = Patient.objects.all()
    return render(request,"patient.html" ,{"doctor_obj":doctor_obj,"patient_obj":patient_obj})

def patient_data(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobileno = request.POST.get('mobileno')
        gender = request.POST.get('gender')
        address = request.POST.get('address')
        dob = request.POST.get('dob')
        report = request.POST.get('report')
        image = request.FILES.get('image')
        dname = request.POST.get('doctor')
        new = Doctor.objects.get(id=dname)
        if Patient.objects.filter(email=email).exists():
            messages.error(request, "Email Already Exists")
        elif Patient.objects.filter(mobileno=mobileno).exists():
            messages.error(request, "Mobile Number Already Register")
        else:
            Patient.objects.create(name=name, email=email,mobileno=mobileno,
                                       gender=gender, address=address,dob=dob,report=report, 
                                       image=image, doctor=new)
            messages.success(request, "Appointment Booked Sucessfully")
            return redirect("/")
        
def patientview(request):
    patient_obj = Patient.objects.all()
    return render(request,"patientview.html",{"patient_obj":patient_obj})

def delete_patient(request,pk):
    Patient.objects.get(id=pk).delete()
    return redirect('/doctorview/')

def doctorlogin(request):
    return render(request,"doctorlogin.html")

def doctor_login(request):
    if request.method == "POST":
        login = Doctor.objects.get(email = request.POST['email'])
        if check_password(request.POST['password'],login.password):
            request.session['login'] = True
            request.session['email'] = login.email
            return redirect('/patientview/')
        else:
            messages.error(request,"Invalid Id Password")
            return redirect("/")
        

def doctorview(request):
    doctor_obj = Doctor.objects.all()
    patient_obj = Patient.objects.all()
    return render(request,"doctorview.html" ,{"doctor_obj":doctor_obj,"patient_obj":patient_obj})

def delete_doctor(request,pk):
    Doctor.objects.get(id=pk).delete()
    return redirect('/doctorview/')

def updatedoctor(request,uid):
    update_doctor=Doctor.objects.get(id=uid)
    return render(request, "updatedoctor.html", {"update_doctor":update_doctor})

def update_doctor(request):
    if request.method == "POST":
        uid = request.POST.get('uid')
        name = request.POST.get('name')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        experience = request.POST.get('experience')
        specialization = request.POST.get('specialization')
        address = request.POST.get('address')
        mobileno = request.POST.get('mobileno')
        password = make_password(request.POST.get('password'))
        degree = request.POST.get('degree')
        image = request.FILES.get('image')
        Doctor.objects.filter(id=uid).update(name=name, email=email,gender=gender,dob=dob,
                                   experience=experience,specialization=specialization,
                                   address=address,mobileno=mobileno,password=password,degree=degree,image=image)
        messages.success(request,"doctor update successfully")
        return redirect("/doctorview/")
        




