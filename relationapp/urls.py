from django.urls import path
from django.http import HttpResponse

def view_test(request):
    return HttpResponse("<h1 align='center'>welcme to the relatioship djano page </h1>")

urlpatterns=[
    path('', view_test)
]