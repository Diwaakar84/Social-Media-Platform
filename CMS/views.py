# from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth import authenticate, login, logout
# from django.contrib import messages

# def welcome_index(request):
#     return render(request, 'welcome/index.html')

# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('welcome_index')
#         else:
#             messages.error(request, 'Invalid username or password.')
#     return render(request, 'sessions/new.html')

# def logout_view(request):
#     logout(request)
#     return redirect('welcome_index')
