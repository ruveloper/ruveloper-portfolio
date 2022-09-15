from django.test import TestCase

from apps.core.models import (
    About,
    Base,
    Company,
    Home,
    Project,
    ResumeEntry,
    Technology,
)


class InitialDataTests(TestCase):
    fixtures = ["default_data.json"]

    def test_create_models(self):
        self.assertEqual(About.objects.count(), 1)
        self.assertEqual(Base.objects.count(), 1)
        self.assertEqual(Home.objects.count(), 1)
        self.assertEqual(Project.objects.count(), 6)
        self.assertEqual(Company.objects.count(), 5)
        self.assertEqual(Technology.objects.count(), 6)
        self.assertEqual(ResumeEntry.objects.count(), 5)
