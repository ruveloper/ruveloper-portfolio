from django.views.generic import TemplateView, ListView, DetailView

from apps.website.models import Base, Home, About, Technology, Project

from apps.website.utils import get_model_or_none


class HomePage(TemplateView):
    template_name = "website/pages/home_page.html"

    def get_context_data(self, **kwargs):
        context = super(HomePage, self).get_context_data(**kwargs)
        # ! ---- CMS Data ----
        context['cms_base']: Base = get_model_or_none(Base)
        context['cms_home']: Home = get_model_or_none(Home)
        return context


class AboutPage(TemplateView):
    template_name = "website/pages/about_page.html"

    def get_context_data(self, **kwargs):
        context = super(AboutPage, self).get_context_data(**kwargs)
        # ! ---- CMS Data ----
        context['cms_base']: Base = get_model_or_none(Base)
        context['cms_about']: About = get_model_or_none(About)
        return context


class ProjectsPage(ListView):
    template_name = 'website/pages/projects_page.html'
    model = Project
    context_object_name = 'cms_projects'

    def get_context_data(self, **kwargs):
        context = super(ProjectsPage, self).get_context_data(**kwargs)
        # ! ---- CMS Data ----
        context['cms_base']: Base = get_model_or_none(Base)
        return context


class ProjectDetailPage(DetailView):
    template_name = 'website/pages/project_detail_page.html'
    model = Project
    context_object_name = 'project'

    def get_context_data(self, **kwargs):
        context = super(ProjectDetailPage, self).get_context_data(**kwargs)
        # ! ---- CMS Data ----
        context['cms_base']: Base = get_model_or_none(Base)
        # * Get previous and next project
        _prev, _next = None, None
        projects = Project.objects.all()
        for i in range(projects.count()):
            if projects[i] == context['project']:
                _prev = projects[i - 1] if (i - 1) >= 0 else None
                _next = projects[i + 1] if (i + 1) < projects.count() else None
                break
        context['prev_project']: Project = _prev
        context['next_project']: Project = _next
        return context


class ContactPage(TemplateView):
    template_name = 'website/pages/contact_page.html'

    def get_context_data(self, **kwargs):
        context = super(ContactPage, self).get_context_data(**kwargs)
        # ! ---- CMS Data ----
        context['cms_base']: Base = get_model_or_none(Base)

        return context
