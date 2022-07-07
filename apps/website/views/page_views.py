from django.views.generic import TemplateView

from apps.website.models import Base, Home

from apps.website.utils import get_model_or_none


class HomePage(TemplateView):
    template_name = "website/pages/home_page.html"

    def get_context_data(self, **kwargs):
        context = super(HomePage, self).get_context_data(**kwargs)
        # ! ---- CMS Data ----
        context['cms_base']:Base = get_model_or_none(Base)
        context['cms_home']:Home = get_model_or_none(Home)
        return context


class AboutPage(TemplateView):
    template_name = "website/pages/about_page.html"

    def get_context_data(self, **kwargs):
        context = super(AboutPage, self).get_context_data(**kwargs)
        # ! ---- CMS Data ----
        context['cms_base']:Base = get_model_or_none(Base)

        return context


class ProjectsPage(TemplateView):
    template_name = 'website/pages/projects_page.html'

    def get_context_data(self, **kwargs):
        context = super(ProjectsPage, self).get_context_data(**kwargs)
        # ! ---- CMS Data ----
        context['cms_base']:Base = get_model_or_none(Base)

        return context


class ProjectDetailPage(TemplateView):
    template_name = 'website/pages/project_detail_page.html'

    def get_context_data(self, **kwargs):
        context = super(ProjectDetailPage, self).get_context_data(**kwargs)
        # ! ---- CMS Data ----
        context['cms_base']:Base = get_model_or_none(Base)

        return context


class ContactPage(TemplateView):
    template_name = 'website/pages/contact_page.html'

    def get_context_data(self, **kwargs):
        context = super(ContactPage, self).get_context_data(**kwargs)
        # ! ---- CMS Data ----
        context['cms_base']:Base = get_model_or_none(Base)

        return context
