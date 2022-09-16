from django.core import mail
from django.test import TestCase
from faker import Faker

from apps.core.models import ContactRecord
from apps.website.forms import ContactRecordForm


class ContactRecordFormTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        faker = Faker()
        cls.test_data = {
            "name": faker.name(),
            "email": faker.email(),
            "subject": faker.sentence(),
            "message": faker.text(),
        }

    def test_valid_form(self):
        form = ContactRecordForm(data=self.test_data)
        self.assertTrue(form.is_valid())

    def test_create_model_on_save(self):
        form = ContactRecordForm(data=self.test_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(ContactRecord.objects.count(), 0)
        form.save()
        self.assertEqual(ContactRecord.objects.count(), 1)

    def test_send_email(self):
        form = ContactRecordForm(data=self.test_data)
        self.assertTrue(form.is_valid())
        # Test there are no messages
        self.assertEqual(len(mail.outbox), 0)
        # Test that one message has been sent.
        form.send_email()
        self.assertEqual(len(mail.outbox), 1)
        # Test content for email sent
        self.assertEqual(
            mail.outbox[0].subject,
            f'[Form contact] {self.test_data["email"]}',
            msg="Fail comparing email subjects, something change in ContactRecordForm?",
        )
