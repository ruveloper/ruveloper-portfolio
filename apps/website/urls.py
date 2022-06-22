from django.urls import path

from apps.website.views import HomePage, AboutPage

app_name = 'website'

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('about/', AboutPage.as_view(), name='about'),
]
