from django.shortcuts import render

from django.views.generic import (
    CreateView
)

from django.views.generic.edit import (
    FormView
)
# Create your views here.
from .forms import UserRegisterForm
#
from .models import User


class UserRegisterView(FormView):
    template_name = "users/register.html"
    form_class = UserRegisterForm
    success_url = '/'

    def form_valid(self, form):
        # 
        User.objects.create_user(

        )                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
        #
        return super(UserRegisterView, self).form_valid(form)
