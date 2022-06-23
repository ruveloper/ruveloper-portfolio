from django.urls import path

from apps.website.views import HomePage, AboutPage, ProjectsPage, ProjectDetailPage, ContactPage

app_name = 'website'

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('about/', AboutPage.as_view(), name='about'),
    path('projects/', ProjectsPage.as_view(), name='projects'),
    path('projects/<str:project_slug>', ProjectDetailPage.as_view(), name='project_detail'),
    path('contact/', ContactPage.as_view(), name='contact'),
]
