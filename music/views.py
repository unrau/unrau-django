from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import MusicEntry

class MusicList(generic.ListView):
    model = MusicEntry
    context_object_name = 'music_list'
    queryset = MusicEntry.objects.filter(status=1).order_by('-pub_date')
    template_name = 'music.html'
    paginate_by = 6

class MusicDetail(generic.DetailView):
    model = MusicEntry
    #context_object_name = 'music_entry'
    template_name = 'music_detail.html'