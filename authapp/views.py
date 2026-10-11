from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate, login,logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def view_home(request):
    return render(request,'authapp/home.html')

# create register view 
def view_regsister(request):
    if request.method == 'GET':
        return render(request, 'authapp/signin.html')

    elif request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['passw']
        pass2 = request.POST['confpassw']

        if pass1 != pass2:
            messages.error(request, "Passwords do not match")
            return render(request, 'authapp/signin.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return render(request, 'authapp/signin.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
            return render(request, 'authapp/signin.html')

        user = User(username=username, email=email)
        user.set_password(pass1)
        user.is_staff = True
        user.is_superuser = True
        user.save()

        messages.success(request, "Admin registration successful!")
        return redirect('login')


# create login views 
def view_Login(request):
        if request.method=="GET":
             return render(request,'authapp/login.html')
        elif request.method=='POST':
            username=request.POST['username']
            password=request.POST['password']
            user=authenticate(request,username=username,password=password)
            if user is not None:
                 login(request,user)
                 return redirect('profile')
            else:
                 messages.success(request,'invailid username and password')
                 return redirect('login')
             
        return(request, 'authapp/login.html')
            

def view_logout(request):
    logout(request)
    return redirect('login')

@login_required
def view_profile(request):
     return render(request,'authapp/profile.html')

@login_required
def view_newpass(request):
    if request.method == "GET":
        return render(request, 'authapp/newpass.html')

    elif request.method == "POST":
        oldpass = request.POST.get('pass')
        newpass = request.POST.get('newpass')
        confpass = request.POST.get('conf')

        if newpass != confpass:
            messages.error(request, "New password and confirm password do not match.")
            return redirect('view_newpass')

        user = request.user
        if not user.check_password(oldpass):
            messages.error(request, "Old password is incorrect.")
            return redirect('view_newpass')

        user.set_password(newpass)
        user.save()
        update_session_auth_hash(request, user)  # Prevents logout after password change
        messages.success(request, "Password changed successfully.")
        return redirect('profile')
          

          
          
