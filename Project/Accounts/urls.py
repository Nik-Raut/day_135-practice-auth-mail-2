
from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views



urlpatterns=[
    path('reg/',registrationview,name='reg'),
    path('login/',loginview,name='login'),
    path('logout/',logoutview,name='logout'),


   ]