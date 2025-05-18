from rest_framework import serializers

from pyd.users.models import User


class UserSerializer(serializers.ModelSerializer[User]):
    class Meta:
        model = User
        fields = ["name", "url"]

        extra_kwargs = {
            "url": {"view_name": "api:user-detail", "lookup_field": "pk"},
        }


class UserDataSerializer(serializers.ModelSerializer[User]):
    class Meta:
        model = User
        fields = ["uuid", "first_name", "last_name", "email", "is_active", "is_staff", "is_superuser", "created_at"]
        read_only_fields = ["uuid", "created_at"]
