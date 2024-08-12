from django.db import models

# Create your models here.

class userdetails(models.Model):
    userphoto = models.ImageField()
    username = models.CharField(max_length=200)
    useremail = models.CharField(max_length=200)
    userphone = models.CharField(max_length=200)
    userpassword = models.CharField(max_length=200)
    



class appoinment_details(models.Model):
    u_id=models.CharField(max_length=100)
    patient_name=models.CharField(max_length=100)
    patient_age=models.CharField(max_length=100)
    patient_phone=models.CharField(max_length=100)
    patient_doctor=models.CharField(max_length=100)
    patient_date=models.CharField(max_length=100)
    patient_problem=models.CharField(max_length=200)

