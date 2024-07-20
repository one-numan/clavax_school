from django.db import models

# Create your models here.
class StudentClass(models.Model):
    """This Model class is for Student's Class | 
    Field are Class Name and Class Discription

    """
    # Class Name : Ist , IInd , IIIrd , IVth
    class_name = models.CharField(max_length=10, unique=True)
    # Class Discription : In this Field / Columns we can store extra information
    class_discription = models.CharField(max_length=200)

    def __str__(self):
        # Dunder Method , In Admin Showing  'Class_name : Class'
        return F'{self.class_name} : Class'

    class Meta:
        # db_table='Class'
        verbose_name = 'Class'
        verbose_name_plural = 'Classes'


class Student(models.Model):
    """This Model Class is for Each Student's Information |
    Field are : First Name , Last Name , Email , Phone , date Of birth , Status , images , Student Class(Foreign Key)

    This Model Model Class make a Class to Student Realtion (one to Many Relation)
    """
    # user = models.ForeignKey(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.BigIntegerField(unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    status = models.BooleanField(default=False)
    images = models.ImageField(
        upload_to='student_images/', blank=True, null=True)
    student_class = models.ForeignKey(StudentClass, on_delete=models.CASCADE)

    def __str__(self):
        return F'{self.first_name} {self.last_name} in Class : {self.student_class}'
