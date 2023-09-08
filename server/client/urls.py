from django.urls import path
from .import views

urlpatterns = [
    path('', views.IndexView, name='index'),
    path('account', views.AccountView, name='account'),
    path('search-results', views.SearchResultsView, name='search-results'),
    path('list-car', views.ListCarView, name='list-car'),
    path('insurance', views.InsuranceView, name='insurance'),
    path('main-search-btn', views.MainSubmitBntView, name='main-search-btn'),
]
