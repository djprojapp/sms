from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from .forms import UserProfileForm, UserUpdateForm
from django.contrib.auth.forms import PasswordChangeForm
from .models import UserProfile
# Create your views here.
def passwordchange(request):
    if request.method == 'POST':
        # Form handling logic for POST request
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your password was successfully updated!')
            return redirect('/')  # Redirect to the home page after successful password change
    else:
        # Display the form for GET request
        form = PasswordChangeForm(request.user)

    return render(request, 'passwordchange.html', {'form': form})

def register(request):
    if request.method=="POST":
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password=request.POST['password']
        p_form=UserProfileForm(request.POST, request.FILES)
        if password==password1:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username already taken")
                return render(request, 'register.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"This email already exists in system")
                return render(request, 'register.html')
            else:
                user=User.objects.create(first_name=first_name, last_name=last_name, username=username, password=make_password(password), email=email)
                user.save()
                p_form=p_form.save(commit=False)
                p_form.user=user
                p_form.save()
                messages.info(request, 'successfuly created')
                return render(request, 'login.html')
        else:
            messages.info(request,"password mis-match")
            return render(request, 'register.html')
    else:
        p_form=UserProfileForm()
        return render(request, 'register.html', {'p_form':p_form})
    
def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.info(request, 'successfuly loged in')
            return redirect('/')
        else:
            messages.info(request, "username or password is incorrect")
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')
    
def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
        messages.info(request, "You are loged out")
        return redirect('/')
    
def userprofile(request):
    if request.method=="POST":
        u_form=UserUpdateForm(request.POST, instance=request.user)
        p_form=UserProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.info(request, "User profile updated successfully")
        return redirect('/')
    else:
        u_form=UserUpdateForm(instance=request.user)
        p_form=UserProfileForm(instance=request.user.userprofile)
        return render(request, 'userprofile.html', {'u_form':u_form, 'p_form':p_form})
    
