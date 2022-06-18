from django.shortcuts import render


# ------------------- ERROR VIEWS -------------------
def error_400(request, exception=None):
    context = {
        "exception":exception,
    }
    return render(request, "400.html", context, status=400)


def error_403(request, exception=None):
    context = {
        "exception":exception,
    }

    return render(request, "403.html", context, status=403)


def error_404(request, exception=None):
    context = {
        "exception":exception,
    }

    return render(request, "404.html", context, status=404)


def error_500(request, exception=None):
    context = {}

    return render(request, "500.html", context, status=500)
