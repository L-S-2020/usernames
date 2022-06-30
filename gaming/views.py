# Importing the authenticate, login, AuthenticationForm, render, redirect, usernames, User, SignUpForm, and messages
# functions from the django.contrib.auth, django.contrib.auth.forms, django.shortcuts, .models,
# django.contrib.auth.models, .forms, and django.contrib modules.
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from .forms import SignUpForm
from .forms import addForm
from .models import usernames


# https://ordinarycoders.com/blog/article/django-user-register-login-logout
# https://www.tabnine.com/
# https://www.jetbrains.com/de-de/pycharm/
# https://plugins.jetbrains.com/plugin/18606-mintlify-doc-writer

# Create your views here.
def profile(request, name):
    """
    It takes a request and a name, gets the user with that name, gets all the games that user has added, and then renders
    the profile page with the name and games.

    :param request: The request is an HttpRequest object. It contains metadata about the request
    :param name: The name of the user whose profile you want to view
    :return: The profile page is being returned.
    """
    me = User.objects.get(username=name)
    names = usernames.objects.filter(author=me)
    return render(request, 'gaming/profile.html', {'name': name, 'games': names})

def edit_profile(request):
    """
    It takes the request, gets the user, and then gets all the games that the user has added to their profile

    :param request: The request is an HttpRequest object
    :return: The user is being returned.
    """
    me = request.user
    if request.user.is_authenticated:
        names = usernames.objects.filter(author=me)
        name = str(me)
        url = request.build_absolute_uri('/profile/' + name)
    else:
        return redirect('login_request')
    return render(request, 'gaming/edit.html', {'name': me, 'games': names, 'url': url})


def add(request):
    if request.method == "POST":
        form = addForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('edit_profile')
    else:
        form = addForm()
    return render(request, 'gaming/add.html', {'form': form})


def delete(request, game):
    me = request.user
    usernames.objects.filter(author=me, game=game).delete()
    return redirect('edit_profile')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "User Account successfully created!")
            return redirect('edit_profile')
        messages.error(request, "Error: User Account could not be created!")
    form = SignUpForm()
    return render(request=request, template_name='gaming/signup.html', context={"register_form": form})


def login_request(request):
    """
    If the request method is POST, then validate the form, and if the form is valid, authenticate the user, and if the user
    is authenticated, log the user in, and if the user is logged in, redirect the user to the homepage, and if the user is
    not logged in, display an error message

    :param request: The request object is passed to the view by Django. It contains all the information about the current
    request
    :return: The login.html page is being returned.
    """
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Welcome {username}.")
                return redirect("edit_profile")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="gaming/login.html", context={"login_form": form})

def logout_request(request):
    logout(request)
    return redirect(login_request)

def home(request):
    return render(request=request, template_name="gaming/main.html")