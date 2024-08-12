"""
URL configuration for kilinik project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('add_doctor',views.add_doctor),
    path('doctor_list',views.doctor_list),
    path('doc_delete/<int:id>',views.doc_delete,name="doc_delete"),
    path('doc_update/<int:id>',views.doc_update,name="doc_update"),
    path('doc_update/doctor_updates/<int:id>',views.doctor_updates,name="doctor_updates"),
    path('admin_view_appointment',views.admin_view_appointment),
    path('admin_home',views.admin_home),
    path('admin_user_list',views.admin_user_list),
    path('admin_user_delete/<int:id>',views.admin_user_delete,name='admin_user_delete'),
    
]
