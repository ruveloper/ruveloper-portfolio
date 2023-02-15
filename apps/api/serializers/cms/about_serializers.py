from rest_framework import serializers

from apps.core.models import About, Company, ResumeEntry


class ResumeEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = ResumeEntry
        fields = (
            "type",
            "title",
            "priority_order",
            "company",
            "start",
            "end",
            "description",
            "project",
        )


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ("name", "priority_order", "logo")


class AboutSerializer(serializers.ModelSerializer):
    company_set = CompanySerializer(many=True, read_only=True)
    resumeentry_set = ResumeEntrySerializer(many=True, read_only=True)
    technology_set = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name="api:technology-detail",
        lookup_field="name",
    )

    class Meta:
        model = About
        fields = (
            "id",
            "language",
            "profile_image",
            "profile_image_webp",
            "body",
            "resumeentry_set",
            "company_set",
            "technology_set",
        )
        read_only_fields = ("profile_image_webp",)
