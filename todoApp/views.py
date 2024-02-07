from django.shortcuts import render, redirect
from .models import *

login_page_url = 'login_page.html'
register_page_url = 'register_page.html'
profile_page_url = 'profile_page.html'
reset_pwd_page_url = 'reset_password_page.html'


def index(request):
    return render(request, login_page_url)

def register_page(request):
    role = Role.objects.all()
    dept = Department.objects.all()

    return render(request, register_page_url, {'roles': role, 'depts': dept})

def reset_password_page(request):
    return render(request, reset_pwd_page_url)

def register(request):
    role = Role.objects.get(id=int(request.POST['roles']))
    dept = Department.objects.get(id=int(request.POST['department']))
    
    master = Master.objects.create(
        Role = role,
        Department = dept,
        Email = request.POST['email'],
        Password = request.POST['password'],
    )

    UserProfile.objects.create(
        Master = master,
    )

    print('account has been created.')
    
    return redirect(index)

def login(request):
    try:
        master = Master.objects.get(Email = request.POST['email'])
        if master.Password == request.POST['password']:
            pass
        else:
            print('incorrect password')
    except Master.DoesNotExist as err:
        print(err)


    return redirect(index)