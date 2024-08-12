from django.shortcuts import render,redirect
from ADMIN.models import doctor_details
from user.models import userdetails
from user.views import *
from ADMIN.views import *

def index(request):
    data=doctor_details.objects.all()
    d_data = doctor_details.objects.count()
    apm = appoinment_details.objects.count()
    value_dict = {"d_data":d_data,
                  "apm":apm,
                  "data":data,
                  }
    return render(request,'index.html',{'result':value_dict})


def login(request):
    useremail = request.POST.get('useremail')
    userpassword = request.POST.get('userpassword')
    if useremail == 'admin@gmail.com' and userpassword =='admin':
        request.session['adminemail'] = useremail
        request.session['admin'] ='admin'
        return redirect(admin_home)
        # return render(request,'admin_home.html',{'status': 'admin login successfull'} )

    elif userdetails.objects.filter(useremail=useremail,userpassword=userpassword).exists():
        udet=userdetails.objects.get(useremail=request.POST['useremail'],userpassword=userpassword)
        if udet.userpassword == request.POST['userpassword']:
            request.session['uid'] = udet.id
            request.session['uname'] = udet.username
            request.session['uemail'] = useremail
            request.session['user'] = 'user'
            return redirect(user_home)
            # return render(request,'user_home.html',{'status': 'user login successfull'})
    else:
          return render(request, 'login.html', {'status': 'incorrect credentials'})
    
def logout(request):
    session_keys = list(request.session.keys())
    for key in session_keys:
        del request.session[key]
    return redirect(index)

def service(request):
    return render(request,'service.html') 

def about_us(request):
    doctor_data = doctor_details.objects.all()
    return render(request,'about_us.html',{'result':doctor_data}) 

def contact_us(request):
    return render(request,'contact_us.html') 
