from django.views.generic import ListView
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from users.models import *
from floreria_chicorita.forms import *
from django.contrib.auth.models import User

def Welcome(request):
	#return HttpResponse(request);
	return render(request,"welcome.html")

def pruebas(request):
	return render(request,"pruebas.html")

def agregarCarrito(request):
	print(request.POST);
	if request.POST:
		formulario = CarritoForm(request.POST)
		if formulario.is_valid():
			usuario = User.objects.get(id=formulario.cleaned_data["idUsuario"])
			arreglo = Inventario.objects.get(id=formulario.cleaned_data["idArregloModl"])
			cantidad = formulario.cleaned_data["cantidad"]
			precio = formulario.cleaned_data["costoArregloModl"]
			compra = Compra()
			compra.user=usuario;
			compra.producto=arreglo;
			compra.cantidad=cantidad;
			compra.precio=precio;
			compra.save()
			messages.success(request,'Se ha agregado el arrego: '+arreglo.nombre+' a su carrito de compras')
			return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
	return render(request,"welcome.html")

def verFlores(request):
	flores = Inventario.objects.all()
	return render(request,"verflores.html",{'flores':flores})