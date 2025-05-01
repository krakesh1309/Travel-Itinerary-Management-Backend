from django.urls import path
from .views import ItineraryList, recommend_itinerary

urlpatterns = [
    path('itineraries/', ItineraryList.as_view()),
    path('recommendations/', recommend_itinerary)
]