# Importing the messages, authenticate, login, logout, AuthenticationForm, User, render, redirect,
# SignUpForm, addForm, and usernames.
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from .forms import SignUpForm
from .forms import addForm
from .models import usernames

# Create your views here.
def profile(request, name):
    # This is the view for the profile page. It is getting the user, getting all the games that user
    # has added, and then rendering the profile page with the name and games.
    me = User.objects.get(username=name)
    names = usernames.objects.filter(author=me)
    return render(request, 'gaming/profile.html', {'name': name, 'games': names})

def edit_profile(request):
    # Getting the user, getting all the games that user has added, and then rendering the profile page
    # with the name and games, if the user is not logged in, it redirects the user to the login page.
    me = request.user
    if request.user.is_authenticated:
        names = usernames.objects.filter(author=me)
        name = str(me)
        url = request.build_absolute_uri('/profile/' + name)
    else:
        return redirect('login_request')
    return render(request, 'gaming/edit.html', {'name': me, 'games': names, 'url': url})


def add(request):
    # This is the view for the add page. It is checking if the request method is POST, if it is, it is
    # getting the form,
    # checking if the form is valid, and if it is, it is saving the form, setting the author to the
    # user, and saving the form.
    # If the form is not valid, it is rendering the add page with the form.
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
    # This is the view for the delete page. It is getting the user, and then deleting the game that
    # the user has added.
    me = request.user
    usernames.objects.filter(author=me, game=game).delete()
    return redirect('edit_profile')


def signup(request):
    # Checking if the request method is POST, if it is, it is getting the form, checking if the form
    # is valid, and if it is, it is saving the form (creating the user account), setting the current user to the new created account, and saving the
    # form. If the form is not valid, it is rendering the add page with the form.
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "User Account successfully created!")
            return redirect('edit_profile')
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")
                print(msg)
        messages.error(request, "Error: User Account could not be created!")
    form = SignUpForm()
    return render(request=request, template_name='gaming/signup.html', context={"register_form": form})

def login_request(request):
    # This is the view for the login page. It is checking if the request method is POST, if it is, it
    # is getting the form, checking if the form is valid, and if it is, it is getting the username and
    # password from the form, authenticating the user, and if the user is not none, it is logging the
    # user in, and redirecting the user to the edit profile page. If the form is not valid, it is
    # rendering the login page with the form.
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
    # Logging the user out and redirecting the user to the login page.
    logout(request)
    return redirect(login_request)

def home(request):
    # Rendering the main page.
    return render(request=request, template_name="gaming/main.html")

def page_not_found_view(request, exception):
    # Rendering the error page with the status 404.
    return render(request=request, template_name='gaming/error.html', status=404)

def r(request):
    # Rickroll somebody.
    return render(request=request, template_name='gaming/fun.html')