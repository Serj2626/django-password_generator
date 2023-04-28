from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'generator/home.html')


def eggs(request):
    return HttpResponse('<h1>Eggs are so tasty</h1>')
