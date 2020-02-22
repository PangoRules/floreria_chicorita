from django.contrib import admin
from django.urls import path
from users.views import *

urlpatterns = [
	path('dashboard/',dashboard,name="dashboard"),
	path('login/',loginuser,name="login"),
	path('register/',register,name="register"),
	path('logout/',logoutuser,name="logout"),
]