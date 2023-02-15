from rest_framework import viewsets

from apps.api.serializers import cms
from apps.core.models import About, Base, Home, Project, Technology


class BaseViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Base.objects.all()
    serializer_class = cms.BaseSerializer


class HomeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Home.objects.all()
    serializer_class = cms.HomeSerializer


class AboutViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = About.objects.all()
    serializer_class = cms.AboutSerializer


class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = cms.ProjectSerializer

    @property
    def get_queryset(self):
        """
        Allow filter project objects by language and count using URL query parameters.
        """
        queryset = Project.objects.all()
        language: str = self.request.query_params.get("language")
        count: str = self.request.query_params.get("count")
        if language:
            queryset = queryset.filter(language=language)
        if count and count.isdecimal() and int(count) > 0:
            queryset = queryset[: int(count)]
        return queryset


class TechnologyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Technology.objects.all()
    serializer_class = cms.TechnologySerializer
    lookup_field = "name"
