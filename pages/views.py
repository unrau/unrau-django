import requests
import os

from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

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

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
