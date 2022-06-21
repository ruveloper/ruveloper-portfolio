from django.views.generic import TemplateView


class HomePage(TemplateView):
    template_name = "website/pages/home_page.html"
