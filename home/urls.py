from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from home import views

urlpatterns = [   
    path("", views.index, name='home'),
    path("TeachReg", views.TeachReg, name='TeachReg'),
    path("StuReg", views.StuReg, name='StuReg'),
    path("tlogin/", views.tlogin, name='tlogin'),
    path("tindex/", views.tindex, name='tindex'),
    path("ass/", views.ass, name='ass'),
    path("slogin/", views.slogin, name='slogin'),
    path("sindex/", views.sindex, name='sindex'),
    path("assStu/", views.assStu, name='assStu'),
    path("submit/", views.submit, name='submit'),
    path("viewsubmissn/", views.viewsubmissn, name='viewsubmissn'),



]+ static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)