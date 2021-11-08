from django.shortcuts import render
from django.contrib.auth.views import LoginView,LogoutView
from exam.models import GeneralInstruction

# Create your views here.

class UserLogin(LoginView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['inst'] = GeneralInstruction.objects.last()
        return context


