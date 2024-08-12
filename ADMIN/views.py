from django.shortcuts import render,redirect
from .models import *
from user.models import appoinment_details,userdetails
# Create your views here.


def add_doctor(request):
    if request.method=="POST":
        doctorphoto = request.FILES['doctorphoto']
        doctorname = request.POST.get('doctorname')
        doctoremail = request.POST.get('doctoremail')
        doctorphone = request.POST.get('doctorphone')
        doctorqualification = request.POST.get('doctorqualification')
        doctor_dutystart = request.POST.get('doctor_dutystart')
        doctor_dutyend = request.POST.get('doctor_dutyend')
        doctor_suggestion = request.POST.get('doctor_suggestion')
        doctor_fees = request.POST.get('doctor_fees')
        doct_db = doctor_details(doctorphoto=doctorphoto,doctorname=doctorname,doctoremail=doctoremail,doctorphone=doctorphone,doctorqualification=doctorqualification,doctor_dutystart=doctor_dutystart,doctor_dutyend=doctor_dutyend,doctor_suggestion=doctor_suggestion,doctor_fees=doctor_fees)
        doct_db.save()
    return render(request,'add_doctor.html')


def doctor_list(request):
    doctor_data = doctor_details.objects.all()
    return render(request,'doctor_list.html',{'result':doctor_data})


def doc_delete(request,id):
    data=doctor_details.objects.get(pk=id)
    data.delete()
    return redirect(doctor_list)

def doc_update(request,id):
    data=doctor_details.objects.get(pk=id)
    return render(request,'doctor_update.html',{'result':data})



def doctor_updates(request,id):
    if request.method=="POST":
        doctorphoto = request.FILES['doctorphoto']
        doctorname = request.POST.get('doctorname')
        doctoremail = request.POST.get('doctoremail')
        doctorphone = request.POST.get('doctorphone')
        doctorqualification = request.POST.get('doctorqualification')
        doctor_dutystart = request.POST.get('doctor_dutystart')
        doctor_dutyend = request.POST.get('doctor_dutyend')
        doctor_suggestion = request.POST.get('doctor_suggestion')
        doctor_fees = request.POST.get('doctor_fees')
        doct_db = doctor_details(id=id,doctorphoto=doctorphoto,doctorname=doctorname,doctoremail=doctoremail,doctorphone=doctorphone,doctorqualification=doctorqualification,doctor_dutystart=doctor_dutystart,doctor_dutyend=doctor_dutyend,doctor_suggestion=doctor_suggestion,doctor_fees=doctor_fees)
        doct_db.save()
        return redirect(doctor_list)
    return render(request,'doctor_update.html')


def admin_view_appointment(request):
    view_app= appoinment_details.objects.all()
    return render(request,'admin_view_appointment.html',{'result':view_app})



def admin_home(request):
    doctor_data = doctor_details.objects.count()
    user_data = userdetails.objects.count()
    apmt_data = appoinment_details.objects.count()
    result = {
        'doctor_data':doctor_data,
        'user_data':user_data,
        'apmt_data':apmt_data,
    }
    return render(request,'admin_home.html',{'result':result})


# user view 
def admin_user_list(request):
    data=userdetails.objects.all()
    return render(request,'admin_user_list.html',{'result':data})

# user delete
def admin_user_delete(request,id):               
    data=userdetails.objects.get(pk=id)
    data.delete()
    return redirect(admin_user_list)

