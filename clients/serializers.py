from django.forms import widgets
from rest_framework import serializers


class ClientSerializer(serializers.Serializer):
    pk = serializers.Field()  # Note: `Field` is an untyped read-only field.
    facebook_id = serializers.CharField(required=True, max_length=255)
    name = serializers.CharField(required=False, max_length=255)
    username = serializers.CharField(required=False, max_length=150)
    gender = serializers.CharField(required=False, max_length=100)

    def restore_object(self, attrs, instance=None):
        if instance:
            instance.facebook_id = attrs.get('facebook_id', instance.facebook_id)
            instance.name = attrs.get('name', instance.name)
            instance.username = attrs.get('username', instance.username)
            instance.gender = attrs.get('gender', instance.gender)
            return instance

        return Client(**attrs)