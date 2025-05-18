from rest_framework import viewsets

from pyd.place.models import Event
from pyd.place.serializers import EventSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
