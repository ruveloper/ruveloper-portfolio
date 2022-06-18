from django.urls import path

from apps.website.views import (
    AboutPage,
    ContactPage,
    HomePage,
    ProjectDetailPage,
    ProjectsPage,
)

app_name = "website"

urlpatterns = [
    path("", HomePage.as_view(), name="home"),
    path("about/", AboutPage.as_view(), name="about"),
    path("projects/", ProjectsPage.as_view(), name="projects"),
    path("projects/<slug:slug>", ProjectDetailPage.as_view(), name="project_detail"),
    path("contact/", ContactPage.as_view(), name="contact"),
    path("contact/success/", ContactPage.as_view(), name="contact_success"),
]
