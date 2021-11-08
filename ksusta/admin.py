from django.contrib import admin
from .models import Facultie,Department,Program

# Register your models here.

my_list = [Department,Facultie,Program]

admin.site.register(my_list)
