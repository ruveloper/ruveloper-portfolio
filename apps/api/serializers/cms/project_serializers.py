from rest_framework import serializers

from apps.core.models import Project


class ProjectSerializer(serializers.ModelSerializer):
    technology_set = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name="api:technology-detail",
        lookup_field="name",
    )

    class Meta:
        model = Project
        fields = (
            "id",
            "language",
            "title",
            "slug",
            "priority_order",
            "link",
            "github_url",
            "cover_image",
            "cover_image_webp",
            "description",
            "activate_details",
            "detail",
            "technology_set",
        )
        read_only_fields = ("cover_image_webp",)
