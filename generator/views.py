from django.shortcuts import render
from django.http import HttpResponse
import random


def home(request):
    '''function to display the home page'''
    return render(request, 'generator/home.html')


def password(request):
    characters = list('abcdefghijklmnoprstuvwxyz')
    length = 10
    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password': thepassword})
