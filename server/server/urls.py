from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('client.urls')),
    path('manager/', include('managers.urls')),
    path('vehicle/', include('vehicle.urls')),
    path('news/', include('news.urls')),
    path('leads/', include('leads.urls')),
    path('search/', include('searchfunction.urls')),
    path('carSearch/', include('carSearch.urls')),
]
