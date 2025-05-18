from rest_framework import serializers

from pyd.core.serializer_utils import BaseSerializer
from pyd.place.models import Calendar
from pyd.place.models import Place


class CalendarSerializer(BaseSerializer, serializers.ModelSerializer):
    place = serializers.PrimaryKeyRelatedField(
        pk_field=serializers.UUIDField(format="hex_verbose"),
        read_only=True,
    )

    class Meta:
        model = Calendar
        fields = "__all__"
