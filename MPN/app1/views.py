from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
from django.contrib import messages


#        ----------Log-in & Sign-up api----------
@login_required
def home(request):
	
    return render(request, 'app1/home.html')

def signupuser(request):
	customer = Customer.objects.all()
	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			
			user = form.save()
			username = form.cleaned_data.get('username')

			Customer.objects.create(
				user=user,
				name=user.username,
				)
			user.save()
			login(request,user)
			return redirect('home')			
	return render(request, 'app1/signupuser.html',{'form':form} )


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'app1/login.html', {'form':AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'app1/login.html', {'form':AuthenticationForm(), 'error':'Error! Try again..'})
        else:
            login(request, user)
            return redirect('home')

@login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('loginuser')


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('about')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'app1/profile.html', context)


@login_required
def about(request):
    
    return render(request, 'app1/about.html')

@login_required
def map(request):
    return render(request, 'app1/map.html')


