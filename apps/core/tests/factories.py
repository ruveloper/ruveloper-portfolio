import random

from django.core.files.uploadedfile import SimpleUploadedFile
from factory.django import DjangoModelFactory
from factory.faker import Faker

from apps.core.models import (
    About,
    Base,
    Company,
    ContactRecord,
    Home,
    Project,
    ResumeEntry,
    Technology,
)
from apps.core.tests.shared import fake_image_bytes


# * ------------ Base Factories ------------
class BaseFactory(DjangoModelFactory):
    email = Faker("email")
    brand = Faker("company")
    logo = SimpleUploadedFile(
        name="logo.jpg", content=fake_image_bytes(300, 300), content_type="image/jpeg"
    )
    favicon = SimpleUploadedFile(
        name="favicon.png", content=fake_image_bytes(32, 32), content_type="image/png"
    )
    github = Faker("url")
    linkedin = Faker("url")

    class Meta:
        model = Base


# * ------------ Base Factories ------------
class HomeFactory(DjangoModelFactory):
    card_title = Faker("sentences", nb=1)
    card_body = Faker("text")
    dev_photo = SimpleUploadedFile(
        name="image.jpg",
        content=fake_image_bytes(512, 512),
        content_type="image/jpeg",
    )

    class Meta:
        model = Home


# * ------------ About Factories ------------
class AboutFactory(DjangoModelFactory):
    profile_image = SimpleUploadedFile(
        name="image.jpg",
        content=fake_image_bytes(512, 512),
        content_type="image/jpeg",
    )
    body = Faker("text")

    class Meta:
        model = About


class CompanyFactory(DjangoModelFactory):
    # about = field (Foreign key relation) need to be passed as parameter in factory create or create_batch methods
    # to avoid use the real database information since these factories are outside the TestCase context
    name = Faker("company")
    logo = SimpleUploadedFile(
        name="image.jpg",
        content=fake_image_bytes(512, 512),
        content_type="image/jpeg",
    )

    class Meta:
        model = Company


class ResumeEntryFactory(DjangoModelFactory):
    # about = field (Foreign key relation) need to be passed as parameter in factory create or create_batch methods
    # to avoid use the real database information since these factories are outside the TestCase context
    title = Faker("sentences", nb=1)
    company = Faker("company")
    start = Faker("date_between")
    description = Faker("text")
    type = random.choice(ResumeEntry.EntryTypes.choices)[0]

    class Meta:
        model = ResumeEntry


# * ------------ About Factories ------------
class ProjectFactory(DjangoModelFactory):
    title = Faker("sentences", nb=1)
    cover_image = SimpleUploadedFile(
        name="image.jpg", content=fake_image_bytes(512, 512), content_type="image/jpeg"
    )
    description = Faker("text")
    detail = Faker("text")

    class Meta:
        model = Project


# * ------------ Technology Factories ------------
class TechnologyFactory(DjangoModelFactory):
    name = Faker("word")
    logo = SimpleUploadedFile(
        name="image.jpg", content=fake_image_bytes(512, 512), content_type="image/jpeg"
    )

    class Meta:
        model = Technology


# * ------------ Contact Record Factories ------------
class ContactRecordFactory(DjangoModelFactory):
    name = Faker("name")
    email = Faker("email")
    subject = Faker("sentence")
    message = Faker("text")

    class Meta:
        model = ContactRecord
