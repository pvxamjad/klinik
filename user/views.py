from django.shortcuts import render,redirect
from . models import *
from ADMIN.models import doctor_details

# Create your views here.

def user_book_appointment(request):
    doc_detail = doctor_details.objects.all()
    u_id=request.session['uid']
    if request.method=="POST":
        patient_name = request.POST.get('patient_name')
        patient_age = request.POST.get('patient_age')
        patient_phone = request.POST.get('patient_phone')
        patient_doctor = request.POST.get('patient_doctor')
        patient_date = request.POST.get('patient_date')
        patient_problem = request.POST.get('patient_problem')
        book_db=appoinment_details(u_id=u_id,patient_name=patient_name,patient_age=patient_age,patient_phone=patient_phone,patient_doctor=patient_doctor,patient_date=patient_date,patient_problem=patient_problem)
        book_db.save()
    return render(request,'user_book_appointment.html',{'result':doc_detail})


def user_view_appointment(request):
    u_id=request.session['uid']
    view_app= appoinment_details.objects.filter(u_id=u_id)
    return render(request,'user_view_appointment.html',{'result':view_app})


def user_profile(request):
    u_id=request.session['uid']
    data=userdetails.objects.get(pk=u_id)
    return render(request,'user_profile.html',{'result':data})

# not required



def user_registration(request):
    if request.method=="POST":
        userphoto = request.FILES["userphoto"]
        username = request.POST.get("username")
        useremail = request.POST.get("useremail")
        userphone = request.POST.get("usermobile")
        userpassword = request.POST.get("userpassword")
        obj = userdetails(userphoto=userphoto,username=username,useremail=useremail,userphone=userphone,userpassword=userpassword)
        obj.save()
    return render(request,'user_registration.html')


def apmt_del(request,id):
    data = appoinment_details.objects.get(pk=id)
    data.delete()
    return redirect(user_view_appointment)

def user_home(request):
    u_id=request.session['uid']
    user=userdetails.objects.get(pk=u_id)
    d_data = doctor_details.objects.count()
    apm = appoinment_details.objects.count()
    value_dict = {"user":user,
                  "d_data":d_data,
                  "apm":apm,
                  }
    return render(request,'user_home.html',{'result':value_dict})

def user_profile_edit(request,id):
    data=userdetails.objects.get(pk=id)
    return render(request,'user_profile_edit.html',{'result':data})

def user_profile_edits(request,id):
    if request.method=="POST":
        userphoto = request.FILES["userphoto"]
        username = request.POST.get("username")
        useremail = request.POST.get("useremail")
        userphone = request.POST.get("usermobile")
        userpassword = request.POST.get("userpassword")
        obj = userdetails(id=id,userphoto=userphoto,username=username,useremail=useremail,userphone=userphone,userpassword=userpassword)
        obj.save()
        return redirect(user_profile)
    return render(request,'user_profile_edit.html')