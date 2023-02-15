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
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.utils.translation import gettext_lazy as _
from filebrowser.sites import site as fb_site

# * Change titles
import apps.website.views

admin.site.site_header = str(_("DEV ADMINISTRATION"))
admin.site.site_title = str(_("DEVELOPER"))
admin.site.index_title = str(_("ADMIN PORTAL"))

# * ---------- URLs -------------
# * Static Url patterns
urlpatterns = [
    path("admin/filebrowser/", fb_site.urls),
    path(settings.ADMIN_URL, admin.site.urls),
    # Django Browser Reload
    path("__reload__/", include("django_browser_reload.urls")),
    # * TinyCME
    path("tinymce/", include("tinymce.urls")),
]

# * I18N URL Patterns
urlpatterns += i18n_patterns(
    # Website URLs
    path("", include("apps.website.urls", namespace="website")),
)

# * API URL Patterns
urlpatterns += [path("api/", include("apps.api.urls", namespace="api"))]

# * -------- ERROR VIEWS --------
handler400 = apps.website.views.error_400_bad_request
handler403 = apps.website.views.error_403_permission_denied
handler404 = apps.website.views.error_404_page_not_found
handler500 = apps.website.views.error_500_server_error

# * -------- DEBUG URLs --------
if settings.DEBUG:
    # * Add URLs for static and media files on development
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    # ! -------- ERROR TEST URLs --------
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            handler400,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            handler403,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            handler404,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", handler500),
    ]
