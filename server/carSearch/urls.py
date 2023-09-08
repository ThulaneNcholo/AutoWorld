from django.urls import path
from .import views

urlpatterns = [
    path('car-search-new', views.CarSearchFilterView, name='car-search-new'),
    path('new-car-results', views.NewResultsView, name='new-car-results'),
    # brand type button search 
    path('new-car-results/<int:id>/<int:type>', views.NewResultsView, name='new-car-results'),

    # HTMX views
    path('new-model', views.NewModelView, name='new-model'),
    path('new-variant-search', views.NewVarientView, name='new-variant-search'),


   
]
