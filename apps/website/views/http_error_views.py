from django.shortcuts import render

from apps.core.models import Base
from apps.core.utils import get_model_or_none


# ------------------- ERROR VIEWS -------------------
def error_400_bad_request(request, exception=None):
    context = {
        "cms_base": get_model_or_none(Base),
        "exception": exception,
    }
    return render(request, "website/errors/400.html", context, status=400)


def error_403_permission_denied(request, exception=None):
    context = {
        "cms_base": get_model_or_none(Base),
        "exception": exception,
    }

    return render(request, "website/errors/403.html", context, status=403)


def error_404_page_not_found(request, exception=None):
    context = {
        "cms_base": get_model_or_none(Base),
        "exception": exception,
    }

    return render(request, "website/errors/404.html", context, status=404)


def error_500_server_error(request, exception=None):
    context = {
        "cms_base": get_model_or_none(Base),
        "exception": exception,
    }
    return render(request, "website/errors/500.html", context, status=500)
