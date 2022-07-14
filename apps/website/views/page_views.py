from django.urls import reverse
from django.views.generic import DetailView, FormView, ListView, TemplateView

from apps.website.forms import ContactRecordForm
from apps.website.models import About, Base, Home, Project
from apps.website.utils import get_model_or_none


class HomePage(TemplateView):
    template_name = "website/pages/home_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # ! ---- CMS Data ----
        context["cms_base"] = get_model_or_none(Base)
        context["cms_home"] = get_model_or_none(Home)
        return context


class AboutPage(TemplateView):
    template_name = "website/pages/about_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # ! ---- CMS Data ----
        context["cms_base"] = get_model_or_none(Base)
        context["cms_about"] = get_model_or_none(About)
        return context


class ProjectsPage(ListView):
    template_name = "website/pages/projects_page.html"
    model = Project
    context_object_name = "cms_projects"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # ! ---- CMS Data ----
        context["cms_base"] = get_model_or_none(Base)
        return context


class ProjectDetailPage(DetailView):
    template_name = "website/pages/project_detail_page.html"
    model = Project
    context_object_name = "project"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # ! ---- CMS Data ----
        context["cms_base"] = get_model_or_none(Base)
        # * Get previous and next project
        _prev, _next = None, None
        projects = Project.objects.all()
        for i in range(projects.count()):
            if projects[i] == context["project"]:
                _prev = projects[i - 1] if (i - 1) >= 0 else None
                _next = projects[i + 1] if (i + 1) < projects.count() else None
                break
        context["prev_project"] = _prev
        context["next_project"] = _next
        return context


class ContactPage(FormView):
    template_name = "website/pages/contact_page.html"
    form_class = ContactRecordForm

    def form_valid(self, form):
        # If form is valid, save record on database and send email
        form.save()
        form.send_email()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("website:contact_success")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # ! ---- CMS Data ----
        context["cms_base"] = get_model_or_none(Base)

        return context
