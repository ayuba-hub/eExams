from django.contrib import admin
from .models import Course,Question,Result,ExamInstruction,GeneralInstruction

# Register your models here.

admin.site.register(Course)
admin.site.register(Question)
admin.site.register(Result)
admin.site.register(ExamInstruction)
admin.site.register(GeneralInstruction)
