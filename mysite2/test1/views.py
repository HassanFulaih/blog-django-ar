from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def my_home(request):
    return HttpResponse('<h1>Home Page</h1>')


def my_contact(request):
    return HttpResponse('<h1>Contact Page</h1>')


def my_index(request):
    return HttpResponse('<h1>Index Page</h1>')
