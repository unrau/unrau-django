from django.contrib import admin
from .models import MusicEntry

class MusicAdmin(admin.ModelAdmin):
    list_display = ('title_text', 'slug', 'pub_date', 'status')
    list_filter = ("status",)
    search_fields = ['title_text', 'content_text']
    prepopulated_fields = {'slug': ('title_text',)}

admin.site.register(MusicEntry, MusicAdmin)