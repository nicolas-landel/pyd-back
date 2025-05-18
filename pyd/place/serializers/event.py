from rest_framework import serializers

from pyd.core.serializer_utils import BaseSerializer
from pyd.place.models import Event
from pyd.place.serializers.tag import EventTagsSerializer


class EventSerializer(BaseSerializer, serializers.ModelSerializer):
    tags = EventTagsSerializer(many=True, read_only=True)

    class Meta:
        model = Event
        fields = "__all__"
        extra_kwargs = {
            "start_date": {"required": True},
            "end_date": {"required": True},
            "place": {"required": True},
            "created_at": {"read_only": True},
            "updated_at": {"read_only": True},
            "uuid": {"read_only": True},
        }
