from django.urls import path
from django.http import HttpResponse
from .views import *



urlpatterns=[
    path('',view_home, name='ahome'),
    path('register/',view_regsister,name='register'),
    path('login/',view_Login,name='login'),
    path('logout/',view_logout,name='logout'),
    path('profile/',view_profile,name='profile'),
    path('newpass/',view_newpass,name='newapp'),
]