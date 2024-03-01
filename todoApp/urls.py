from .views import *
from django.urls import path

urlpatterns = [
    path('', index, name='login_page'),
    path('register_page/', register_page, name='register_page'),
    path('reset_password_page/', reset_password_page, name='reset_password_page'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('profile_page/', profile_page, name='profile_page'),
    path('profile_update/', profile_update, name='profile_update'),
    path('upload_profile_image/', upload_profile_image, name='upload_profile_image'),
    
    path('add_task/', add_task, name='add_task'),

    path('logout/', logout, name='logout'),
]