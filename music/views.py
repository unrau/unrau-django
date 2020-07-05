from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import MusicEntry

class MusicList(generic.ListView):
    queryset = MusicEntry.objects.filter(status=1).order_by('-pub_date')
    template_name = 'index.html'

class MusicDetail(generic.DetailView):
    model = MusicEntry
    template_name = 'music_detail.html'