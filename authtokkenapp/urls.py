from django.urls import path
from django.http import HttpResponse
from .views import *


urlpatterns=[
    path('',register, name='register'),
    path('login/',View_login,name='login'),
    path('logout/',view_logout,name='logout'),
    path('home/',view_home,name='home'),
    path('change_password/', view_change_password, name="changepass"),
] 