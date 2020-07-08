#
from django.urls import path

from . import views

app_name = 'users_app'

urlpatterns = [
    path(
        'register/',
        views.UserRegisterView.as_view(),
        name='user-register'
    ),
    path(
        'login/',
        views.LoginUser.as_view(),
        name='login'
    ),
    path(
        'logout/',
        views.LogoutView.as_view(),
        name='user-logout'
    ),
    path(
        'update_password/',
        views.UpdatePasswordView.as_view(),
        name='user-update'
    ),
    path(
        'user-verificacion/<pk>/',
        views.CodeVerificacionView.as_view(),
        name='user-verificacion'
    ),
]
