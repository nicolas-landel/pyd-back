from rest_framework import serializers

from pyd.core.serializer_utils import BaseSerializer
from pyd.place.models import Calendar
from pyd.place.models import Event
from pyd.place.models import EventTags
from pyd.place.models import Tag


class TagSerializer(BaseSerializer, serializers.ModelSerializer):
    calendar = serializers.PrimaryKeyRelatedField(
        queryset=Calendar.objects.all(),
        pk_field=serializers.UUIDField(format="hex_verbose"),
    )

    class Meta:
        model = Tag
        fields = "__all__"
        extra_kwargs = {
            "name": {"required": True},
            "description": {"required": False},
            "created_at": {"read_only": True},
            "updated_at": {"read_only": True},
            "uuid": {"read_only": True},
        }


class EventTagsSerializer(serializers.ModelSerializer):
    tag = serializers.PrimaryKeyRelatedField(
        queryset=Tag.objects.all(), pk_field=serializers.UUIDField(format="hex_verbose")
    )
    event = serializers.PrimaryKeyRelatedField(
        queryset=Event.objects.all(),
        pk_field=serializers.UUIDField(format="hex_verbose"),
    )

    class Meta:
        model = EventTags
        fields = "__all__"
        extra_kwargs = {
            "event": {"required": True},
            "tag": {"required": True},
            "uuid": {"read_only": True},
        }
