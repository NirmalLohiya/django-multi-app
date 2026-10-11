from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, UserLoginForm, UserPassworchangeForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import CustomUser


def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # Extract cleaned data from the form
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # Use the CustomUserManager to create the user
            user = CustomUser.objects.create_user(username=username, email=email, password=password)
            user.save()

            messages.success(request, "Registration successful. You can now login.")
            return redirect('login')
        else:
            messages.error(request, "There was an error with your registration form.")
    else:
        form = UserRegistrationForm()
    
    return render(request, 'authtokkenapp/register.html', {"form": form})


def View_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            print(f"Username: {username}, Password: {password}")  # Debugging
            
            # Check if the user exists
            try:
                user = CustomUser.objects.get(username=username)
                print(f"User found: {user}")  # Debugging
            except CustomUser.DoesNotExist:
                print("User does not exist")  # Debugging 
                user = None
            user = authenticate(request, username=username, password=password)
            print(f"Authenticated User: {user}")  # Debugging
            
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Form is not valid.")
    else:
        form = UserLoginForm()
    
    return render(request, 'authtokkenapp/login.html', {"form": form})


@login_required
def view_home(request):
    return render(request, 'authtokkenapp/home.html')


def view_logout(request):
    logout(request)
    return redirect('login')

def view_change_password(request):
    form=UserPassworchangeForm(request.GET)
    d1={'form':form}
    return redirect(request,'authtokkenapp/change_password.html', context=d1)
    # if request.method =='GET':
    #     return redirect(request, 'authtokkenapp/change_password.html')
    # elif request.method =='POST':
    #     form=UserPassworchangeForm(request.POST)
    #     pass
        

