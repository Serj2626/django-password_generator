from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    '''function to display the home page'''
    return render(request, 'generator/home.html')


def password(request):
    return render(request, 'generator/password.html')
