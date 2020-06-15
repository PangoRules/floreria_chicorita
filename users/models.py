from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

class Inventario(models.Model):
	nombre = models.CharField(max_length=250,blank=False, null=False)
	descripcion = models.CharField(max_length=250,blank=False, null=False)
	stock = models.IntegerField(blank=False, null=False)
	precio = models.IntegerField(blank=False, null=False)
	flor_pic = models.ImageField(null=True, blank=True)

	def __str__(self):
		return self.nombre
	


class Compra(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE,blank=False, null=False)
	producto = models.ForeignKey(Inventario,on_delete=models.CASCADE,blank=False, null=False)
	fecha = models.DateField(default=datetime.now)
	cantidad = models.IntegerField(null=True, blank=True)
	precio = models.IntegerField(null=True, blank=True)
	esta_en_carro = models.BooleanField(default=True,blank=True, null=True)
	def __str__(self):
		return self.user.username + " - " + self.producto.nombre


