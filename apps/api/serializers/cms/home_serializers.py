from rest_framework import serializers

from apps.core.models import Home, Service


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ("title", "priority_order", "description", "fa_icon")


class HomeSerializer(serializers.ModelSerializer):
    service_set = ServiceSerializer(many=True, read_only=True)

    class Meta:
        model = Home
        fields = (
            "id",
            "language",
            "card_title",
            "card_body",
            "dev_photo",
            "dev_photo_webp",
            "contact_msg",
            "service_set",
        )
        read_only_fields = ("dev_photo_webp",)
