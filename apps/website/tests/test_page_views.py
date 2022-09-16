from django.template.response import TemplateResponse
from django.test import TestCase
from django.urls import reverse

from apps.core.models import About, Base, Home, Project
from apps.website.forms import ContactRecordForm


class PageViewTests(TestCase):
    def test_home_page_view(self):
        url = reverse("website:home")
        resp: TemplateResponse = self.client.get(url)  # noqa
        self.assertEqual(resp.status_code, 200)
        self.assertTrue("cms_base" in resp.context_data.keys())
        self.assertTrue("cms_home" in resp.context_data.keys())
        self.assertTemplateUsed(
            response=resp, template_name="website/pages/home_page.html"
        )

    def test_about_page_view(self):
        url = reverse("website:about")
        resp: TemplateResponse = self.client.get(url)  # noqa
        self.assertEqual(resp.status_code, 200)
        self.assertTrue("cms_base" in resp.context_data.keys())
        self.assertTrue("cms_about" in resp.context_data.keys())
        self.assertTemplateUsed(
            response=resp, template_name="website/pages/about_page.html"
        )

    def test_projects_page_view(self):
        url = reverse("website:projects")
        resp: TemplateResponse = self.client.get(url)  # noqa
        self.assertEqual(resp.status_code, 200)
        self.assertTrue("cms_base" in resp.context_data.keys())
        self.assertTemplateUsed(
            response=resp, template_name="website/pages/projects_page.html"
        )

    def test_contact_page_view(self):
        url = reverse("website:contact")
        resp: TemplateResponse = self.client.get(url)  # noqa
        self.assertEqual(resp.status_code, 200)
        self.assertTrue("cms_base" in resp.context_data.keys())
        self.assertTemplateUsed(
            response=resp, template_name="website/pages/contact_page.html"
        )


class PageContentTests(TestCase):
    # Load initial model data from core.fixtures to test view content
    fixtures = ["default_data.json"]

    def test_home_page_content(self):
        url = reverse("website:home")
        resp: TemplateResponse = self.client.get(url)  # noqa
        self.assertEqual(resp.status_code, 200)
        self.assertIsNotNone(resp.context_data["cms_base"])
        self.assertIsInstance(resp.context_data["cms_base"], Base)
        self.assertIsNotNone(resp.context_data["cms_home"])
        self.assertIsInstance(resp.context_data["cms_home"], Home)

    def test_about_page_content(self):
        url = reverse("website:about")
        resp: TemplateResponse = self.client.get(url)  # noqa
        self.assertEqual(resp.status_code, 200)
        self.assertIsNotNone(resp.context_data["cms_base"])
        self.assertIsInstance(resp.context_data["cms_base"], Base)
        self.assertIsNotNone(resp.context_data["cms_about"])
        self.assertIsInstance(resp.context_data["cms_about"], About)

    def test_projects_page_content(self):
        url = reverse("website:projects")
        resp: TemplateResponse = self.client.get(url)  # noqa
        self.assertEqual(resp.status_code, 200)
        self.assertIsNotNone(resp.context_data["cms_base"])
        self.assertIsInstance(resp.context_data["cms_base"], Base)
        # * Test list model objects
        self.assertIsNotNone(resp.context_data["cms_projects"])
        self.assertEqual(resp.context_data["cms_projects"].count(), 6)
        self.assertIsInstance(resp.context_data["cms_projects"].first(), Project)

    def test_project_detail_content(self):
        second_project: Project = Project.objects.all()[1]
        url = reverse("website:project_detail", kwargs={"slug": second_project.slug})
        resp: TemplateResponse = self.client.get(url)  # noqa
        self.assertEqual(resp.status_code, 200)
        self.assertIsNotNone(resp.context_data["cms_base"])
        self.assertIsInstance(resp.context_data["cms_base"], Base)
        # * Test model objects
        self.assertIsNotNone(resp.context_data["project"])
        self.assertIsInstance(resp.context_data["project"], Project)
        self.assertIsNotNone(resp.context_data["prev_project"])
        self.assertIsInstance(resp.context_data["prev_project"], Project)
        self.assertIsNotNone(resp.context_data["next_project"])
        self.assertIsInstance(resp.context_data["next_project"], Project)

    def test_contact_content(self):
        url = reverse("website:contact")
        resp: TemplateResponse = self.client.get(url)  # noqa
        self.assertEqual(resp.status_code, 200)
        self.assertIsNotNone(resp.context_data["cms_base"])
        self.assertIsInstance(resp.context_data["cms_base"], Base)
        # * Test form content
        self.assertIsNotNone(resp.context_data["form"])
        self.assertIsInstance(resp.context_data["form"], ContactRecordForm)
