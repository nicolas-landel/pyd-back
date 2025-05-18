from rest_framework import serializers


class BaseSerializer(metaclass=serializers.SerializerMetaclass):
    created_by = serializers.UUIDField(read_only=True)
    modified_by = serializers.UUIDField(read_only=True)
    uuid = serializers.UUIDField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        validated_data = self._prefill_validated_data(validated_data)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        validated_data = self._prefill_validated_data(validated_data, instance=instance)
        return super().update(instance, validated_data)

    def get_user_uuid(self):
        print("CCCCCCC", dir(self.context))
        request = self.context.get("request")
        if (
            not request
            or not hasattr(request, "user")
            or not request.user.is_authenticated
        ):
            return None
        return getattr(request.user, "uuid", None) or getattr(request.user, "id", None)

    def _prefill_validated_data(self, validated_data, instance=None):
        if not (user_uuid := self.get_user_uuid()):
            return validated_data

        validated_data = validated_data.copy()

        if instance:
            validated_data["modified_by"] = user_uuid
            validated_data["created_by"] = instance.created_by
        else:
            validated_data["created_by"] = user_uuid
        return validated_data
