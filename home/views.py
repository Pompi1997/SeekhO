from pydoc import classname
from django.shortcuts import render
from django.contrib import messages
from home.models import  Classroom, Student, Teacher,Assignment, stuAssign
from os import name
from django.core.exceptions import ObjectDoesNotExist
from unicodedata import name
from django.core import paginator
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth.hashers import make_password,check_password
from datetime import *
from django.http import request, response
from django.shortcuts import render,redirect
from django.http import HttpResponse

from django.contrib.auth import authenticate , login

from django.core.paginator import EmptyPage, InvalidPage, Paginator
# Create your views here.

def index(request):
    return render(request, 'index.html')

def TeachReg(request):

    tea=Classroom.objects.all()
    if request.method == "POST":
        tname = request.POST.get('Tname')
        tpwd = request.POST.get('Tpwd')
        cName = request.POST.get('className')            #taking class name from Teacher form
        classN = Classroom.objects.get(className=cName)  #checking the classname of form by comparing classroom classname and teacher foreign key classname
        tform = Teacher(Teachername=tname, Teacherpwd=tpwd, className=classN)
        tform.save()
        messages.success(request, 'Your form has been submitted.')
    return render(request, 'TeachReg.html',{"tea":tea})


def StuReg(request):
    stu=Classroom.objects.all()
    if request.method == "POST":
        Sname = request.POST.get('Sname')
        Spwd = request.POST.get('Spwd')
        cName = request.POST.get('className')            #taking class name from Teacher form
        classN = Classroom.objects.get(className=cName)
        sform = Student(Sname=Sname, Spwd=Spwd, className=classN)
        sform.save()
        messages.success(request, 'Your form has been submitted.')
    return render(request, 'StuReg.html',{"stu":stu})

def slogin(request):
    if  request.method == "POST":
         Sname = request.POST['Sname']
         spassword = request.POST['Spwd']
         request.session['Sname']=Sname
         try:
             s=Student.objects.get(Sname=Sname, Spwd=spassword)
             print(s.className)
             return render(request, "sindex.html",{"student":Sname,"sclass":s.className})

         except ObjectDoesNotExist:
            print("wrong Password")
            messages.warning(request, 'Wrong Entry')
            return redirect('slogin')
    else:
            return render(request, 'slogin.html')

def tlogin(request):
    if  request.method == "POST":
        tusername = request.POST['Tname']
        tpassword = request.POST['Tpwd']
        request.session['tusername']=tusername
        try:
             t=Teacher.objects.get(Teachername=tusername, Teacherpwd=tpassword)
             print(t.className)
             return render(request, "tindex.html",{"Teacher":tusername,"tclass":t.className})

        except ObjectDoesNotExist:
            print("wrong Password")
            messages.warning(request, 'Wrong Entry')
            return redirect('tlogin')

    else:
        return render(request, 'tlogin.html')


def sindex(request):
    Sname=request.session.get('Sname')

    return render(request,'sindex.html',{"student":Sname})


def tindex(request):
    tname=request.session.get('tusername')

    return render(request,'tindex.html',{"Teacher":tname})


        
def tindex(request):
    tname=request.session.get('tusername')

    return render(request,'tindex.html',{"Teacher":tname})
    
def ass(request):
    tname=request.session.get('tusername')

    t=Teacher.objects.get(Teachername=tname)
    print(t.className)
        
    ass=Classroom.objects.all()
    if request.method == 'POST':
        assname=request.POST.get('assname')
        assclass_id= request.POST.get('assclass')
        assclass= Classroom.objects.get(className=assclass_id)
        assfile=request.FILES['assfile']
        tname=request.POST.get('tname')
        assnotice=request.POST.get('assnotice')

        assignment=Assignment(Aname=assname,Afile=assfile,className=assclass,Teachername=tname,Notice=assnotice)
        assignment.save()
        return redirect('ass')
    else:
        return render(request,'ass.html',{"ass":ass,"tname":tname,"cl":t.className})


def assStu(request):
    if request.method == "POST":
        sclass_id= request.POST.get("sclass")
        assclass= Classroom.objects.get(className=sclass_id)
        print(assclass)
        show=Assignment.objects.filter(className=assclass)
        return render(request,'assStu.html',{"show":show})
    else:
        return render(request,'assStu.html')


# def viewsubmissn(request):
#     if request.method == "POST":
#         class_id= request.POST.get("tclass")
#         assclass= Classroom.objects.get(className=class_id)
#         print(assclass)
#         show=stuAssign.objects.filter(className=assclass)
#         return render(request,'viewsubmissn.html',{"show":show})
#     else:
#         return render(request,'viewsubmissn.html')

def viewsubmissn(request):

    # show=stuAssign.objects.all()

    if request.method == "POST":
        cls=request.POST.get('class')
        cls1= Classroom.objects.get(className=cls)
        print(cls1)
        show=stuAssign.objects.filter(className=cls1)

    return render(request,'viewsubmissn.html',{"show":show})


def submit(request):
    sname=request.session.get('Sname')

    s=Student.objects.get(Sname=sname)
    print(s.className)
        
    ass=Classroom.objects.all()
    if request.method == 'POST':
        assname=request.POST.get('assname')
        assclass_id= request.POST.get('assclass')
        assclass= Classroom.objects.get(className=assclass_id)
        assfile=request.FILES['assfile']
        sname=request.POST.get('Sname')
        assignment=stuAssign(Aname=assname,Sfile=assfile,className=assclass,studentname=sname)
        assignment.save()
        return redirect('submit')
    else:
        return render(request,'submit.html',{"ass":ass,"sname":sname,"cl":s.className})


