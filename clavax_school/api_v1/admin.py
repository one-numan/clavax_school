from django.contrib import admin
from .models import Student, StudentClass


class ClassAdmin(admin.ModelAdmin):
    """Customized Style in Admin Panel"""
    list_display = ('class_name', 'class_discription')


# Student's Profile Class Register in the Admin Panel
admin.site.register(Student) 


# Student's Class Register in the Admin Panel | Give the access to Admin Portal for this Student Class
admin.site.register(StudentClass, ClassAdmin)
