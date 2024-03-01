from django.shortcuts import render, redirect
from .models import *
from django.conf import settings
from datetime import datetime

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

    if user_profile.BirthDate:
        user_profile.BirthDate =  user_profile.BirthDate.strftime("%Y-%m-%d")

    default_data['profile_data'] = user_profile
    default_data['gender_choices'] = gender_choices

    all_user_profiles = UserProfile.objects.all()

    task_members = list()
    for member in all_user_profiles:
        if member.id != user_profile.id:
            task_members.append(member)

    default_data['all_members'] = task_members
    
    default_data['task_list'] = ToDoList.objects.all()

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

import os
print(os.scandir(os.path.join(settings.MEDIA_ROOT, 'users/avatars')))

# change profile image
def upload_profile_image(request):
    master = Master.objects.get(Email=request.session['email'])
    user = UserProfile.objects.get(Master = master)

    user.ProfileImage = request.FILES['profile_image']

    img = request.FILES['profile_image']
    
    full_name = user.FullName.split()
    full_name = '_'.join(full_name)

    new_name = f'{full_name}_{user.Mobile}.{img.name.split(".")[-1]}'
    img.name = new_name
    file_path = os.path.join(settings.MEDIA_ROOT, 'users/avatars')
    main_path = os.scandir(file_path)

    for file in main_path:
        if img.name in file.name:
            os.remove(os.path.join(file_path, img.name))
    
    user.save()

    return redirect(profile_page)

# change password
def change_password(request):
    # write your code here
    
    return redirect(profile_page)

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

# profile update
def profile_update(request):
    master = Master.objects.get(Email=request.session['email'])
    user = UserProfile.objects.get(Master=master)

    user.FullName = request.POST['full_name']
    user.Mobile = request.POST['mobile']
    user.Country = request.POST['country']
    user.State = request.POST['state']
    user.City = request.POST['city']
    user.BirthDate = request.POST['birth_date']
    user.Gender = request.POST['gender']

    user.save()

    return redirect(profile_page)
    

# add task
def add_task(request):
    master = Master.objects.get(Email=request.session['email'])
    date = request.POST['date'].split('-')
    time = request.POST['time'].split(':')
    
    deadline = datetime(int(date[0]), int(date[1]), int(date[2]), int(time[0]), int(time[1]))

    todo = ToDoList.objects.create(
        Title = request.POST['task_title'],
        Tags = request.POST['tags'],
        Deadline = request.POST['date'],
        Description = request.POST['description'],
    )

    members = request.POST['members']
    for member in members:
        user = UserProfile.objects.get(id=int(member))
        TaskAssociation.objects.create(
            Member = user,
            ToDoList = todo,
        )

    print(deadline)
    print(request.POST)
    return redirect(profile_page)

# logout
def logout(request):
    if 'email' in request.session:
        del request.session['email']
    
    return redirect(index)