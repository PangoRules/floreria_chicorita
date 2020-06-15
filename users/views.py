from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from .forms import CreateUserForm
from .models import Inventario, Compra

# Create your views here.

@login_required(login_url='login')
def dashboard(request):
	if request.user.is_authenticated:
		pedidos = Compra.objects.filter(user=request.user,esta_en_carro=False).order_by('fecha')
		return render(request,"users/dashboard.html",{'compras':pedidos})
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

def carrito(request):
	carrito = Compra.objects.filter(user=request.user,esta_en_carro=True).order_by('fecha')

	if request.method=="POST":
		carrito = Compra.objects.filter(user=request.user,esta_en_carro=True)

		if not carrito:
			messages.success(request,'Su carro esta vacio')
			return render(request,"users/carrito.html")

		if request.POST['opcSelec'] == "comprar":
			for item in carrito:
				item.esta_en_carro=False
				item.save()

			messages.success(request,'Se ha realizado tu operacion con exito')
			return render(request,"users/carrito.html")

		else:
			for item in carrito:
				item.delete()
			messages.success(request,'Se han eliminado los items de su carrito ')
			return render(request,"users/carrito.html")
	return render(request,"users/carrito.html",{'carrito':carrito})