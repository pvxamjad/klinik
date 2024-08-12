from django.db import models

# Create your models here.


class doctor_details(models.Model):
    doctorphoto = models.ImageField()
    doctorname = models.CharField(max_length=200)
    doctoremail = models.CharField(max_length=200)
    doctorphone = models.CharField(max_length=200)
    doctorqualification = models.CharField(max_length=200)
    doctor_dutystart = models.CharField(max_length=200)
    doctor_dutyend = models.CharField(max_length=200)
    doctor_suggestion = models.CharField(max_length=200)
    doctor_fees = models.CharField(max_length=100)

