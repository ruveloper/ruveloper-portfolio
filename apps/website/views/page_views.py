from typing import Optional

from django.conf import settings
from django.db import models
from django.http import Http404
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, FormView, ListView, TemplateView

from apps.core.models import About, Base, Home, Project
from apps.core.utils import get_model_or_none, get_model_with_lang
from apps.website.forms import ContactRecordForm
from apps.website.utils import validate_recaptcha_token


class HomePage(TemplateView):
    template_name = "website/pages/home_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # ! ---- CMS Data ----
        context["cms_base"] = get_model_or_none(Base)
        context["cms_home"] = get_model_with_lang(
            Home, self.request.LANGUAGE_CODE  # type: ignore
        )
        context["cms_projects"] = Project.objects.filter(language=self.request.LANGUAGE_CODE)[:3]  # type: ignore
        if settings.DEBUG:
            return context
        # ! ---- Google Services  ----
        context["g_tag_id"] = settings.GOOGLE_TAG_ID
        return context


class AboutPage(TemplateView):
    template_name = "website/pages/about_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # ! ---- CMS Data ----
        context["cms_base"] = get_model_or_none(Base)
        context["cms_about"] = get_model_with_lang(
            About, self.request.LANGUAGE_CODE  # type: ignore
        )
        if settings.DEBUG:
            return context
        # ! ---- Google Services  ----
        context["g_tag_id"] = settings.GOOGLE_TAG_ID
        return context


class ProjectsPage(ListView):
    template_name = "website/pages/projects_page.html"
    model = Project
    context_object_name = "cms_projects"

    def get_queryset(self):
        return self.model.objects.filter(language=self.request.LANGUAGE_CODE)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # ! ---- CMS Data ----
        context["cms_base"] = get_model_or_none(Base)
        if settings.DEBUG:
            return context
        # ! ---- Google Services  ----
        context["g_tag_id"] = settings.GOOGLE_TAG_ID
        return context


class ProjectDetailPage(DetailView):
    template_name = "website/pages/project_detail_page.html"
    model = Project
    context_object_name = "project"

    def get_queryset(self):
        return self.model.objects.filter(slug=self.kwargs["slug"])

    def get_object(self, queryset: Optional[models.query.QuerySet[Project]] = None) -> Project:  # fmt:skip
        if queryset is None:
            queryset = self.get_queryset()
        # Get first the model that meets the requested language code and slug (filter from the queryset),
        # if not exists, try to return in other language
        obj = queryset.filter(
            language=self.request.LANGUAGE_CODE,  # type: ignore
        ).first()
        if obj:
            return obj
        return super().get_object(queryset=queryset)

    def get_context_data(self, **kwargs):
        # ! ---- Check if active ----
        if not self.object.activate_details:
            raise Http404

        context = super().get_context_data(**kwargs)
        # ! ---- CMS Data ----
        context["cms_base"] = get_model_or_none(Base)
        # * Get previous and next project
        _prev, _next = None, None
        projects = Project.objects.filter(
            language=self.request.LANGUAGE_CODE,  # type: ignore
            activate_details=True,
        )
        for i in range(projects.count()):
            if projects[i] == context["project"]:
                _prev = projects[i - 1] if (i - 1) >= 0 else None
                _next = projects[i + 1] if (i + 1) < projects.count() else None
                break
        context["prev_project"] = _prev
        context["next_project"] = _next
        if settings.DEBUG:
            return context
        # ! ---- Google Services  ----
        context["g_tag_id"] = settings.GOOGLE_TAG_ID
        return context


class ContactPage(FormView):
    template_name = "website/pages/contact_page.html"
    form_class = ContactRecordForm

    def form_valid(self, form):
        if settings.DEBUG:
            return super().form_valid(form)
        # * ---- reCaptcha validation ----
        recaptcha_token: Optional[str] = self.request.POST.get("g-recaptcha-response")
        success, score = validate_recaptcha_token(recaptcha_token)
        if success and score >= settings.RECAPTCHA_REQUIRED_SCORE:
            # On form and reCaptcha valid, save record on database and send email
            form.save()
            form.send_email()
            return super().form_valid(form)
        # ! On reCaptcha not valid, return a non field error
        form.add_error(None, _("Invalid reCaptcha, please try again."))
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse("website:contact_success")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # ! ---- CMS Data ----
        context["cms_base"] = get_model_or_none(Base)
        if settings.DEBUG:
            return context
        # ! ---- Google Services  ----
        context["g_tag_id"] = settings.GOOGLE_TAG_ID
        context["g_recaptcha_publickey"] = settings.RECAPTCHA_PUBLIC_KEY
        return context
