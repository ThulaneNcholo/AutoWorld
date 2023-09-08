from django.urls import path
from .import views

urlpatterns = [
    path('list-leads', views.ListLeadsView, name='list-leads'),
]
