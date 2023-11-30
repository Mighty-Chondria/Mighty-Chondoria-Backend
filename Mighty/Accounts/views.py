from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.conf import settings
from django.http import HttpResponse
import datetime
from django.contrib.auth.decorators import login_required
from django.conf.urls import handler404, handler500

from django.http import HttpResponse

from django import forms
from .models import UserAdmin
from .forms import AdminForm,LoginForm





def courses(request):
    """Process images uploaded by users"""
    language_code = request.path.split('/')[1]  # Extract the first part of the path
    # load the home background
    """Process images uploaded by users"""
    # load the home background
    template_name = 'course.html' if language_code == 'en' else 'course.html'
    return render(request, template_name,
                  { "language_code": language_code, })



def immunology(request):
    language_code = request.path.split('/')[1]  # Extract the first part of the path
# if request.user.is_subscriped:
    print(request.user.is_subscriped)
    template_name = 'detail - Immunology.html' if language_code == 'en' else 'detail - Immunology.html'
    return render(request, template_name,
                {"language_code": language_code, })
# else:
    print("not subscriped")
    return render(request, '404.html',
        {"language_code": language_code, })
    



def hematology(request):
    """Process images uploaded by users"""
    language_code = request.path.split('/')[1]  # Extract the first part of the path

    """Process images uploaded by users"""
    # load the home background
    template_name = 'detail - hematology.html' if language_code == 'en' else 'detail - hematology.html'
    return render(request, template_name,
                  { "language_code": language_code, })

def about_us(request):
    """Process images uploaded by users"""
    language_code = request.path.split('/')[1]  # Extract the first part of the path

    template_name = 'about.html' if language_code == 'en' else 'about-ar.html'
    homeinfo = HomeInfo.objects.get(pk=1)
    return render(request, template_name,
                  { "language_code": language_code, 'home_background': home_background})





# Create an error message function
def get_error_message(request):
    password1 = request.POST['password1']
    password2 = request.POST['password2']
    email = request.POST['email']
    if password1 != password2:
        return "The Passwords didn't match"
    if UserAdmin.objects.filter(email=email).exists():
        return "Email already exists"


# Create your views here.

def register_request(request):
    language_code = request.path.split('/')[1]  # Extract the first part of the path
    # load the home background

    template_name = 'register.html' if language_code == 'en' else 'register-ar.html'
   
    if request.method == "POST":
        form = AdminForm(request.POST)
        if form.is_valid():
            user = form.save()

            messages.success(request, "Register successful")
            return redirect(f'/{language_code}/')

        messages.error(request, get_error_message(request))
        return render(request, template_name, context={'register_form': form, "language_code": language_code,
                                                        })
    else:
        form = AdminForm()
        return render(request, template_name, context={'register_form': form, "language_code": language_code,
                                                        })

def logout_request(request):
    logout(request)
    messages.info(request, "You have sucessfully logged out")
    return redirect("login")


# Create your views here.
def login_request(request):
    language_code = request.path.split('/')[1]  # Extract the first part of the path
    # load the home background

    template_name = 'login.html' if language_code == 'en' else 'login-ar.html'

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)

            # username=form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            # user=authenticate(username=username,password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are logged in as {username}")
                return redirect(f'/{language_code}/')
            else:
                messages.error(request, "Invalid username and password!")
        else:
            messages.error(request, "Invalid form")

    form = LoginForm()
    return render(request, template_name,
                  context={'login_form': form, "language_code": language_code})


def logout_request(request):
    logout(request)
    messages.info(request, "You have sucessfully logged out")
    return redirect("login")

@login_required(login_url='/ar/login/')
def home_page(request):
    language_code = request.path.split('/')[1]  # Extract the first part of the path
    template_name = 'home.html' if language_code == 'en' else 'home-ar.html'


    return render(request, template_name,
                  { "language_code": language_code,
                  })


def about(request):
    language_code = request.path.split('/')[1]  # Extract the first part of the path
    # load the home background

    return render(request, 'about.html', context={"language_code": language_code, 'home_background': home_background})


def contactus(request):
    language_code = request.path.split('/')[1]  # Extract the first part of the path


    template_name = 'contact.html' if language_code == 'en' else 'contact-ar.html'
    return render(request, template_name, context={"language_code": language_code})


def contacts_page(request):
    language_code = request.path.split('/')[1]  # Extract the first part of the path
    # load the home background


    template_name = 'users_data.html' if language_code == 'en' else 'users_data-ar.html'
    usersdata = UserContact.objects.all().order_by('-created')
    return render(request, template_name,
                  {"usersdata": usersdata, "language_code": language_code})



def custom_404_view(request, exception=None):
    return render(request, '404.html', status=404)


def custom_500_view(request):
    return render(request, '500.html', status=500)
