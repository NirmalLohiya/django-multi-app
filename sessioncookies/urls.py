from django.urls import path
from .views import *


urlpatterns=[
    path('set/',set_session,name='setsession'),
    path('get/',get_session,name='getsession'),
    path('delete/',delete_session,name='deletesession'),
]
