from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.api.viewsets import cms_viewsets

app_name = "api"

router = DefaultRouter()
router.register("cms/base", cms_viewsets.BaseViewSet)
router.register("cms/home", cms_viewsets.HomeViewSet)
router.register("cms/about", cms_viewsets.AboutViewSet)
router.register("cms/projects", cms_viewsets.ProjectViewSet, basename="project")
router.register("cms/technologies", cms_viewsets.TechnologyViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
