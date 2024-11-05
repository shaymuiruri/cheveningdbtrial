from django.shortcuts import render
# from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import UserRegisterForm
def home(request):
    return render(request, 'dbusers/home.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi {username} your account was created successfully')
            return redirect('home')
            # return redirect(request, 'dbusers/register_success.html')
        #  else:
        #     return render(request, 'dbusers/register_failure.html')
    else:
        form = UserRegisterForm() 
    return render(request, 'dbusers/register.html', {'form': form})

def login(request):
    return render(request, 'dbusers/login.html')

def logout(request):
     return render(request, 'dbusers/logout.html')   

def profile(request):
    return render(request, 'dbusers/profile.html')

# def reset_password(request):
#     return render(request, 'dbusers/reset_password.html')

# def change_password(request):
#     return render(request, 'dbusers/change_password.html')

# def delete_account(request):
#     return render(request, 'dbusers/delete_account.html')   

# def update_profile(request):
#     return render(request, 'dbusers/update_profile.html')

# def update_profile_picture(request):
#     return render(request, 'dbusers/update_profile_picture.html')

# def register_success(request):
#     return render(request, 'dbusers/register_success.html')

# def login_success(request):
#     return render(request, 'dbusers/login_success.html')

# def logout_success(request):
#     return render(request, 'dbusers/logout_success.html')

# def register_failure(request):
#     return render(request, 'dbusers/register_failure.html')

# def login_failure(request):
#     return render(request, 'dbusers/login_failure.html')

# def logout_failure(request):
#     return render(request, 'dbusers/logout_failure.html')

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, 'You have been logged out successfully.')
        return redirect('dbusers:home')  # Adjust this according to your URL configuration
    return redirect('dbusers:home')  # Redirect if accessed via GET
