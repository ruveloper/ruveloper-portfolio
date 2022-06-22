from django.urls import path

from apps.website.views import HomePage, AboutPage, ProjectsPage, ProjectDetailPage

app_name = 'website'

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('about/', AboutPage.as_view(), name='about'),
    path('projects/', ProjectsPage.as_view(), name='projects'),
    path('projects/<str:project_slug>', ProjectDetailPage.as_view(), name='project_detail'),
]
