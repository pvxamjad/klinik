from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    
    path('user_registration',views.user_registration),
    path('user_book_appointment',views.user_book_appointment),
    path('user_view_appointment',views.user_view_appointment),
    path('user_profile',views.user_profile),
    path('appointment_delete/<int:id>',views.apmt_del,name="apmt_del"),
    path('user_home',views.user_home,),
    path('user_profile_edit/<int:id>',views.user_profile_edit,name="user_profile_edit"),
    path('user_profile_edit/user_profile_edits/<int:id>',views.user_profile_edits,name="user_profile_edits"),
]