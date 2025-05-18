from django.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter

from pyd.place.views import CalendarViewSet
from pyd.place.views import EventViewSet
from pyd.place.views import PlaceViewSet
from pyd.place.views import TagViewSet

router = DefaultRouter()
router.register(r"places", PlaceViewSet, basename="place")
router.register(r"events", EventViewSet, basename="event")
router.register(r"calendars", CalendarViewSet, basename="calendar")
router.register(r"tags", TagViewSet, basename="tag")

urlpatterns = [
    path("", include(router.urls)),
]
