from rest_framework import viewsets

from pyd.place.models import Place
from pyd.place.serializers import PlaceSerializer


class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
