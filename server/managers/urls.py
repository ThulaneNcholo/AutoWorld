from django.urls import path
from .import views

# images urls
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('inventory', views.CarsView, name='inventory'),
    path('upload', views.UploadCarView, name='upload'),

    # htmx
    path('filter-model', views.CarModelsView, name='filter-model'),
    path('filter-variant', views.CarVariantsView, name='filter-variant'),
    path('features-filter', views.CarFeaturesView, name='features-filter'),
    path('add-feature', views.AddFeatureView, name='add-feature'),
    path('create-feature', views.CreateNewFeatureView, name='create-feature'),
    path('city-filter', views.CityFilterView, name='city-filter'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
