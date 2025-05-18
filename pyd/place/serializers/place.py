from rest_framework import serializers

from pyd.core.serializer_utils import BaseSerializer
from pyd.place.models import Place


class PlaceSerializer(BaseSerializer, serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = "__all__"
        extra_kwargs = {
            "name": {"required": True},
            "description": {"required": False},
            "location": {"required": True},
            "created_at": {"read_only": True},
            "updated_at": {"read_only": True},
            "uuid": {"read_only": True},
        }
