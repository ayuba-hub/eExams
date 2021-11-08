from django.db import models
from django.contrib.auth.models import User
from ksusta.models import Department,Facultie,Program

# Create your models here.


CHOICES = (('matric','MATRIC'),('ijmb','IJMB'),('nd1','ND1'),('ug1','UG1'))

class StudentProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=20,default='')
    middle_name = models.CharField(max_length=20,default='',blank=True,null=True)
    lastname = models.CharField(max_length=20,default='')
    profile_picture = models.ImageField(upload_to='profile_pics',default='pics')
    admission_number = models.CharField(max_length=10)
    faculty = models.ForeignKey(Facultie,on_delete=models.CASCADE)
    department = models.ForeignKey(Department,on_delete=models.CASCADE)
    program = models.ForeignKey(Program,on_delete=models.CASCADE)
    level = models.CharField(max_length=6,choices=CHOICES,default="UG1")

    def __str__(self):
        return self.admission_number
    

