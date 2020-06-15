from django.views.generic import ListView
from django.shortcuts import render
from django.http import HttpResponse
from users.models import *

def Welcome(request):
	#return HttpResponse(request);
	return render(request,"welcome.html")

def pruebas(request):
	return render(request,"pruebas.html")

def verflores(request):
	return render(request,"verflores.html")