from django.urls import path
from .import views

urlpatterns = [
    path('car-details/<int:id>', views.CarDetailView, name='car-details'),
    path('message/<int:id>', views.MessageView, name='message'),
]
