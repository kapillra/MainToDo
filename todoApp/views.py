from django.shortcuts import render

login_page_url = 'login_page.html'
register_page_url = 'register_page.html'
profile_page_url = 'profile_page.html'
reset_pwd_page_url = 'reset_password_page.html'


def index(request):
    return render(request, login_page_url)

def register_page(request):
    return render(request, register_page_url)

def reset_password_page(request):
    return render(request, reset_pwd_page_url)

def register(request):
    pass