from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Itinerary
from .serializers import ItinerarySerializer

class ItineraryList(generics.ListCreateAPIView):
    queryset = Itinerary.objects.all()
    serializer_class = ItinerarySerializer


@api_view(['GET'])
def recommend_itinerary(request):
    nights = int(request.GET.get('nights',0))
    itineraries = Itinerary.objects.filter(nights=nights)
    serializer = ItinerarySerializer(itineraries, many=True)
    return Response(serializer.data)