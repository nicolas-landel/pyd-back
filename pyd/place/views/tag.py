from rest_framework import viewsets

from pyd.place.models import Tag
from pyd.place.serializers import TagSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
