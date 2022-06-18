from django.urls import path

from apps.website.views import HomePage

app_name = "website"

urlpatterns = [
    path("", HomePage.as_view(), name="home"),
]
