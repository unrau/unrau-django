from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import KnotEntry

class KnotList(generic.ListView):
    model = KnotEntry
    context_object_name = 'knot_list'
    queryset = KnotEntry.objects.filter(status=1).order_by('-pub_date')
    template_name = 'knot.html'
    paginate_by = 1

class KnotDetail(generic.DetailView):
    model = KnotEntry
    template_name = 'knot_detail.html'