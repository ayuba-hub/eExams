from django.db import models

# Create your models here.

class Facultie(models.Model):
    name_of_faculty = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name_of_faculty}'

class Department(models.Model):
    Faculty = models.ForeignKey(Facultie,on_delete=models.CASCADE)
    department_name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.department_name}'

class Program(models.Model):
    faculty = models.ForeignKey(Facultie,on_delete=models.CASCADE)
    department = models.ForeignKey(Department,on_delete=models.CASCADE)
    official_title = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.official_title}'




