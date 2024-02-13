from django.shortcuts import render, redirect
from .models import *

login_page_url = 'login_page.html'
register_page_url = 'register_page.html'
profile_page_url = 'profile_page.html'
reset_pwd_page_url = 'reset_password_page.html'

default_data = {}

def index(request):
    return render(request, login_page_url)

def register_page(request):
    role = Role.objects.all()
    dept = Department.objects.all()

    return render(request, register_page_url, {'roles': role, 'depts': dept})

def reset_password_page(request):
    return render(request, reset_pwd_page_url)


# load profile data
def profile_data(request):
    master = Master.objects.get(Email=request.session['email'])
    user_profile = UserProfile.objects.get(Master=master)

    default_data['profile_data'] = user_profile

    print('profile data called')

def profile_page(request):
    if 'email' in request.session:
        profile_data(request)
        return render(request, profile_page_url, default_data)
    return redirect(index)


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
            request.session['email'] = master.Email
            return redirect(profile_page)
        else:
            print('incorrect password')
    except Master.DoesNotExist as err:
        print(err)


    return redirect(index)

# logout
def logout(request):
    if 'email' in request.session:
        del request.session['email']
    
    return redirect(index)