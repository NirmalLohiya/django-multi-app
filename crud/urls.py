from django.urls import path
from .views import *


urlpatterns=[
    path('',view_page),
    path('employee/', employee,name='employee'),
    path('createEmp/', CreateEmp,name='createEmp'),
    path('showdata/',showData,name='showdata'),
    path('updatedata/<int:id>/',updateEmp,name='update'),
    path('deleteemp/<int:id>/',deleteEmp,name='delete')
]
