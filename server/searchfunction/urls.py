from django.urls import path
from .import views

urlpatterns = [
    path('main-search', views.CarSearchResultsView, name='main-search'),

    path('search-page', views.NewFilterTest, name='search-page'),
    path('cars-results', views.CarsResultsView, name='cars-results'),
    path('cars-results/<int:id>/<int:brand>', views.CarsResultsView, name='cars-results'),

    path('cars-model', views.ModelCarView, name='cars-model'),
    path('cars-variants', views.VariantsCarsView, name='cars-variants'),

    # refine
    path('refine-model', views.RefineModelView, name='refine-model'),
    path('refine-variant', views.RefineVariantView, name='refine-variant'),


    path('cars-data', views.CarsDataView, name='cars-data'),

    path('redirect-form', views.RedirectFormView, name='redirect-form'),
]
