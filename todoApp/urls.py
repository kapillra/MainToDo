from .views import *
from django.urls import path

urlpatterns = [
    path('', index, name='login_page'),
    path('register_page/', register_page, name='register_page'),
    path('reset_password_page/', reset_password_page, name='reset_password_page'),
]