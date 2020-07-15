from django.urls import path
from . import views

urlpatterns = [
    path('', views.KnotList.as_view(), name='knot'),
    path('<slug:page_num>/', views.KnotDetail.as_view(), name='knot_detail'),
]   