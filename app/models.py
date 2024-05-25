from django.db import models
#from .models import Doctor, Patient # Assuming doctor_models.py contains the Doctor model definition

# Create your models here.

class AdminSignup(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    mobileno = models.IntegerField()
    password = models.CharField(max_length=220)

    def __str__(self):
        return str(self.name)
    
class Doctor(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    gender = models.CharField(max_length=200)
    dob = models.DateField()
    experience = models.CharField(max_length=200)
    specialization = models.CharField(max_length=200)
    address = models.TextField()
    mobileno = models.BigIntegerField()
    password = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    image = models.ImageField(upload_to='Doctore',max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.name)


class Patient(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    mobileno = models.BigIntegerField()
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    gender = models.CharField(max_length=200)
    address = models.TextField()
    dob = models.DateField()
    report = models.DateField()
    image = models.FileField(upload_to='Patient', max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.name)


    

        
