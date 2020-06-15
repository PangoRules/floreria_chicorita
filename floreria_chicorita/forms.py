from django import forms
from django.forms import ModelForm
from users.models import *

class CarritoForm(forms.Form):
	idUsuario = forms.CharField(required=True)
	idArregloModl = forms.CharField(required=True)
	nomArregloModl = forms.CharField(required=True)
	costoArregloModl = forms.DecimalField(required=True)
	cantidad = forms.DecimalField(required=True)