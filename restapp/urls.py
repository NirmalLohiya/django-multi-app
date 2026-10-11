from django.urls import path
from .views import *




urlpatterns=[
    # path('', employeeListcreate.as_view(),name='employess_create'),
    path('employee',create_employee, name='create'),
    path('employee_detail/<int:id>/',employee_details,name='employee_detail')
]