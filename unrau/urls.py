from django.urls import path, include
from django.contrib import admin

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()

import pages.views

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("", pages.views.index, name="index"),
    path("apps", pages.views.apps, name="apps"),
    path("comics", pages.views.comics, name="comics"),
    path("contact", pages.views.contact, name="contact"),
    path("keybender", pages.views.keybender, name="keybender"),
    path("admin/", admin.site.urls),
    path("blog/", include('blog.urls')),
    path("music/", include('music.urls')),
    path('summernote/', include('django_summernote.urls')),
]

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
