import requests
import os

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def apps(request):
    return render(request, 'apps.html', {})

def contact(request):
    return render(request, 'contact.html', {})

def comics(request):
    return render(request, 'comics.html', {})

def keybender(request):
    return render(request, 'keybender.html', {})
