from rest_framework import serializers

from apps.core.models import Base


class BaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Base
        exclude = ("created", "modified")
