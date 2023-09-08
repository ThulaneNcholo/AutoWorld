from django.urls import path
from .import views

urlpatterns = [
    path('latest-news', views.NewsView, name='latest-news'),
]
