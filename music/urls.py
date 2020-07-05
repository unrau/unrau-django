from django.urls import path
from . import views

urlpatterns = [
    path('', views.MusicList.as_view(), name='music'),
    path('<slug:slug>/', views.MusicDetail.as_view(), name='music_detail'),
]