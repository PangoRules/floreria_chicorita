from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from .forms import CreateUserForm

# Create your views here.

@login_required(login_url='login')
def dashboard(request):
	if request.user.is_authenticated:
		return render(request,"users/dashboard.html")
	return redirect('/login')

def register(request):
	if request.user.is_authenticated:
		return redirect('dashboard')
	else:
		form = CreateUserForm()
		if request.method=='POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request,'Cuenta creada con exito para: '+user)
				return redirect('login')
	return render(request, "users/register.html",{'form':form})

def loginuser(request):
	if request.user.is_authenticated:
		return redirect('dashboard')
	else:
		form = AuthenticationForm()
		if request.method=="POST":
			form = AuthenticationForm(data=request.POST)
			if form.is_valid():
				username = form.cleaned_data['username']
				password = form.cleaned_data['password']

				user = authenticate(username=username, password=password)

				if user is not None:
					login(request,user)
					return redirect('dashboard')
	return render(request, "users/login.html", {'form':form})

def logoutuser(request):
	logout(request)
	return redirect('login')