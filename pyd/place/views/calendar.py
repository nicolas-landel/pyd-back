from rest_framework import viewsets

from pyd.place.models import Calendar
from pyd.place.serializers import CalendarSerializer


class CalendarViewSet(
    viewsets.ReadOnlyModelViewSet,
):
    queryset = Calendar.objects.all()
    serializer_class = CalendarSerializer
