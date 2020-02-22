from django.views.generic import ListView
from django.shortcuts import render
from django.http import HttpResponse

def Welcome(request):
	return render(request,"welcome.html")

def pruebas(request):
	return render(request,"pruebas.html")