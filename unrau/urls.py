from django.urls import path, include
from django.contrib import admin

# TEST
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# ENDTEST

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
    path("db/", pages.views.db, name="db"),
    path("admin/", admin.site.urls),
    path("blog/", include('blog.urls')),
]
urlpatterns += staticfiles_urlpatterns()
