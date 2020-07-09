from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import BlogEntry

class BlogList(generic.ListView):
    model = BlogEntry
    context_object_name = 'blog_list'
    queryset = BlogEntry.objects.filter(status=1).order_by('-pub_date')
    template_name = 'blog.html'
    paginate_by = 6

class BlogDetail(generic.DetailView):
    model = BlogEntry
    template_name = 'blog_detail.html'