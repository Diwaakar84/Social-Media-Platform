from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import logout, authenticate, login as auth_login
from django.contrib import messages
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import UserRegisterForm

def welcome_index(request):
    return render(request, 'welcome/index.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/sign_up.html', {'form': form, 'title':'register here'})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth_login(request, user)
                messages.success(request, f'Welcome {username}!')
                return redirect('welcome_index')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    
    else:
        form = AuthenticationForm()

    return render(request, 'registration/login.html', {'form': form, 'title': 'Log In'})

def logout_view(request):
    logout(request)
    return redirect('welcome_index')