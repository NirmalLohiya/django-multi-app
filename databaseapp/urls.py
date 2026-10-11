from django.urls import path
from django.http import HttpResponse

def view_test(request):
    return HttpResponse("<h1 align='center'>this is databases app test</h1>")

urlpatterns=[
    path('',view_test)
]