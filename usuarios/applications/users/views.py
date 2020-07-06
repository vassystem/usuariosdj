from django.shortcuts import render

from django.views.generic import (
    CreateView
)
# Create your views here.
from .forms import UserRegisterForm

class UserRegisterView(CreateView):
    template_name = "users/register.html"
    form_class = UserRegisterForm
    success_url = '/'