from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def view_signal(request):
    return HttpResponse("<h1>this is the single logic base page!!!</h1>")


