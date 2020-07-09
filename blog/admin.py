from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import BlogEntry

class BlogAdmin(SummernoteModelAdmin):
    list_display = ('title_text', 'slug', 'pub_date', 'status')
    list_filter = ("status",)
    search_fields = ['title_text', 'content_text']
    prepopulated_fields = {'slug': ('title_text',)}
    summernote_fields = ('content_text',)

admin.site.register(BlogEntry, BlogAdmin)
