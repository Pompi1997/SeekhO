from django.contrib import admin
from home.models import  Classroom, Student, Teacher,Assignment,stuAssign
# Register your models here.
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Classroom)
admin.site.register(Assignment)
admin.site.register(stuAssign)