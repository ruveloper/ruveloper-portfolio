from django.views.generic import TemplateView


class HomePage(TemplateView):
    template_name = "website/pages/home_page.html"


class AboutPage(TemplateView):
    template_name = "website/pages/about_page.html"


class ProjectsPage(TemplateView):
    template_name = 'website/pages/projects_page.html'


class ProjectDetailPage(TemplateView):
    template_name = 'website/pages/project_detail_page.html'


class ContactPage(TemplateView):
    template_name = 'website/pages/contact_page.html'

