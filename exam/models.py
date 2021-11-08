from django.db import models
from accounts.models import StudentProfile
from django.utils import timezone


class Course(models.Model):
    time_in_munites = models.IntegerField(default=0)
    course_code = models.CharField(max_length=200,default='')
    course_name = models.CharField(max_length=50)
    question_number = models.PositiveIntegerField()
    total_marks = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.course_code.upper()}'

class Question(models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    marks=models.PositiveIntegerField()
    question=models.CharField(max_length=600)
    option1=models.CharField(max_length=200)
    option2=models.CharField(max_length=200)
    option3=models.CharField(max_length=200)
    option4=models.CharField(max_length=200)

    cat=(('Option1','Option1'),('Option2','Option2'),('Option3','Option3'),('Option4','Option4'))
    answer=models.CharField(max_length=200,choices=cat)

    def __str__(self):
        return f'{self.question}'

class ExamInstruction(models.Model):
    course_title = models.ForeignKey(Course,on_delete=models.CASCADE)
    instruction = models.TextField(max_length=200)

    def __str__(self):
        return self.course_title

class GeneralInstruction(models.Model):
    title = models.CharField(max_length=100,help_text='exam rules,sitting rules')
    instruction = models.TextField(max_length=3000)

    def __str__(self):
        return f'{self.title.upper()}'

class Result(models.Model):
    student = models.ForeignKey(StudentProfile,on_delete=models.CASCADE)
    exam = models.ForeignKey(Course,on_delete=models.CASCADE)
    marks = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now=True)

