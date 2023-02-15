from rest_framework import serializers

from apps.core.models import Technology, TechnologyDescription


class TechnologyDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechnologyDescription
        fields = ("language", "description")


class TechnologySerializer(serializers.ModelSerializer):
    technologydescription_set = TechnologyDescriptionSerializer(
        many=True, read_only=True
    )

    class Meta:
        model = Technology
        fields = ("id", "name", "priority_order", "logo", "technologydescription_set")
