"""portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views import defaults as default_views
from django.utils.translation import gettext_lazy as _

# ? Change titles
admin.site.site_header = str(_('DEV ADMINISTRATION'))
admin.site.site_title = str(_('DEVELOPER'))
admin.site.index_title = str(_('ADMIN PORTAL'))

# ? ---------- URLs -------------
urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),

    # Django Browser Reload
    path("__reload__/", include("django_browser_reload.urls")),

    # ? CKEditor
    path('ckeditor/', include('ckeditor_uploader.urls')),

    # Website URLs
    path('', include('apps.website.urls', namespace='website')),
]

# ? -------- ERROR VIEWS --------
handler400 = 'apps.website.views.error_400'
handler403 = 'apps.website.views.error_403'
handler404 = 'apps.website.views.error_404'
handler500 = 'apps.website.views.error_500'

# ? -------- DEBUG URLs --------
if settings.DEBUG:
    # ? Add URLs for static and media files on development
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    # ! -------- ERROR TEST URLs --------
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path("400/", default_views.bad_request, kwargs={"exception":Exception("Bad Request!")}, ),
        path("403/", default_views.permission_denied, kwargs={"exception":Exception("Permission Denied")}, ),
        path("404/", default_views.page_not_found, kwargs={"exception":Exception("Page not Found")}, ),
        path("500/", default_views.server_error),
    ]
