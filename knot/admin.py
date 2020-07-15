from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import KnotEntry

class KnotAdmin(SummernoteModelAdmin):
    list_display = ('title_text', 'page_num', 'pub_date', 'status')
    list_filter = ("status",)
    search_fields = ['title_text', 'content_text']
    summernote_fields = ('content_text',)

admin.site.register(KnotEntry, KnotAdmin)