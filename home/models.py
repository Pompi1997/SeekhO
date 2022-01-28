from django.db import models
from django.contrib import admin
# Create your models here.
from statistics import mode
from django.db import models
from django.utils import timezone

# model for classroom
class Classroom(models.Model):
    className=models.CharField(max_length=12)
    Desc=models.CharField(max_length=200,null=True)
    def __str__(self):
        return self.className

# model For Teacher
class Teacher(models.Model):
    className=models.ForeignKey(Classroom,related_name='forAA', on_delete=models.CASCADE)
    Teachername=models.CharField(max_length=122,null=False)
    Teacherpwd=models.CharField(max_length=12,null=False)
    
    def __str__(self):
        return self.Teachername


# model For Student
class Student(models.Model):
    sid=models.AutoField(primary_key=True)
    Sname=models.CharField(max_length=122,null=False)
    Spwd=models.CharField(max_length=12,null=False)
    className=models.ForeignKey(Classroom,related_name='forA', on_delete=models.CASCADE)
    def __str__(self):
        return self.Sname



# model for assignments uploaded by teacher for respective classrooms

class Assignment(models.Model):
    Aname=models.CharField(max_length=100,null=False)
    Afile=models.FileField(upload_to='media')
    className=models.ForeignKey(Classroom,related_name='forAAA', on_delete=models.CASCADE)
    Teachername=models.CharField(max_length=100,null=False)
    Notice=models.CharField(max_length=200,null=True)
    created_at=models.DateField(default=timezone.now)
    def __str__(self):
        return self.Aname

# model for assignments uploaded by students for respective classrooms

class stuAssign(models.Model):
    Aname=models.CharField(max_length=100,null=False)
    Sfile=models.FileField(upload_to='submissions')
    className=models.ForeignKey(Classroom,related_name='foreign', on_delete=models.CASCADE)
    studentname=models.CharField(max_length=100,null=False)
    created_at=models.DateField(default=timezone.now)
    def __str__(self):
        return self.Aname
 