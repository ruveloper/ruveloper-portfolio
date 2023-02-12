from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import SimpleUploadedFile
from django.db import IntegrityError
from django.test import TestCase
from PIL import Image

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
from apps.core.tests.factories import (
    AboutFactory,
    BaseFactory,
    CompanyFactory,
    ContactRecordFactory,
    HomeFactory,
    ProjectFactory,
    ResumeEntryFactory,
    TechnologyFactory,
)
from apps.core.tests.shared import (
    clean_media_test_folder,
    fake_file_bytes,
    fake_image_bytes,
    fake_string,
)


class BaseModelTests(TestCase):
    base = None

    @classmethod
    def setUpTestData(cls) -> None:
        # Initial model object.
        cls.base = BaseFactory.create()

    @classmethod
    def tearDownClass(cls):
        # * ---- Clean execution at the end ----
        super().tearDownClass()
        clean_media_test_folder()

    def test_create_model(self):
        # Assert model object was created.
        self.assertEqual(Base.objects.count(), 1)

    def test_singleton_model(self):
        # Check raise exception when triying to create a second model object.
        self.assertRaises(IntegrityError, BaseFactory.create)

    def test_max_length(self):
        # Test max length for char fields
        with self.assertRaises(ValidationError) as raised:
            self.base.email = f"{fake_string(260)}@mail.com"
            self.base.brand = fake_string(260)
            self.base.full_clean()  # noqa
        raised_msg: dict = raised.exception.message_dict
        self.assertTrue("email" in raised_msg.keys())
        self.assertTrue("at most 255" in raised_msg["email"][0])
        self.assertTrue("brand" in raised_msg.keys())
        self.assertTrue("at most 255" in raised_msg["brand"][0])

    def test_max_file_size(self):
        # Text max size for file-based fields
        with self.assertRaises(ValidationError) as raised:
            self.base.logo = SimpleUploadedFile(
                name="logo.svg", content=fake_file_bytes(150), content_type="image/svg"
            )
            self.base.favicon = SimpleUploadedFile(
                name="favicon.jpg",
                content=fake_file_bytes(20),
                content_type="image/jpeg",
            )
            self.base.full_clean()  # noqa
        raised_msg: dict = raised.exception.message_dict
        self.assertTrue("logo" in raised_msg.keys())
        self.assertTrue("Max file size" in raised_msg["logo"][0])
        self.assertTrue("favicon" in raised_msg.keys())
        self.assertTrue("Max file size" in raised_msg["favicon"][0])

    def test_valid_image(self):
        # Test if uploaded image is a valid image (no corrupt content)
        with self.assertRaises(ValidationError) as raised:
            self.base.logo = SimpleUploadedFile(
                name="logo.jpg", content=fake_file_bytes(0), content_type="image/jpeg"
            )
            self.base.full_clean()  # noqa
        raised_msg: dict = raised.exception.message_dict
        self.assertTrue("logo" in raised_msg.keys())
        self.assertTrue("invalid or corrupt" in raised_msg["logo"][0])


class HomeModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Initial model object
        cls.home: Home = HomeFactory.create()

    @classmethod
    def tearDownClass(cls):
        # * ---- Clean execution at the end ----
        super().tearDownClass()
        clean_media_test_folder()

    def test_create_model(self):
        self.assertEqual(Home.objects.count(), 1)

    def test_auto_generate_webp(self):
        # Test if the webp version of dev_photo is autogenerate
        webp_img = self.home.dev_photo_webp
        self.assertIsNotNone(webp_img.name)
        # Check webp_img had valid content
        Image.open(self.home.dev_photo_webp.file)


class AboutModelsTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Initial model objects
        cls.about: About = AboutFactory.create()
        # ! Since Company and ResumeEntry need an About Model relation, we need to pass the relation to the factory
        # ! to ensure don't create another About object outside the TestCase context (and Temporal Test Database)
        CompanyFactory.create_batch(7, about=cls.about)
        ResumeEntryFactory.create_batch(7, about=cls.about)
        cls.company: Company = Company.objects.first()
        cls.resume_entry: ResumeEntry = ResumeEntry.objects.first()

    @classmethod
    def tearDownClass(cls):
        # * ---- Clean execution at the end ----
        super().tearDownClass()
        clean_media_test_folder()

    def test_create_models(self):
        self.assertEqual(About.objects.count(), 1)
        self.assertEqual(Company.objects.count(), 7)
        self.assertEqual(ResumeEntry.objects.count(), 7)

    def test_max_file_size(self):
        upload_img = SimpleUploadedFile(
            name="image.jpg",
            content=fake_image_bytes(9000, 9000),
            content_type="image/jpeg",
        )
        with self.assertRaises(ValidationError) as raised:
            self.about.profile_image = upload_img
            self.about.full_clean()  # noqa
        raised_msg: dict = raised.exception.message_dict
        self.assertTrue("profile_image" in raised_msg.keys())
        self.assertTrue("Max file size" in raised_msg["profile_image"][0])

        with self.assertRaises(ValidationError) as raised:
            self.company.logo = upload_img
            self.company.full_clean()  # noqa
        raised_msg: dict = raised.exception.message_dict
        self.assertTrue("logo" in raised_msg.keys())
        self.assertTrue("Max file size" in raised_msg["logo"][0])

    def test_auto_generate_webp(self):
        webp_img = self.about.profile_image_webp
        self.assertIsNotNone(webp_img.name)
        Image.open(self.about.profile_image_webp.file)


class ProjectModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Initial model object
        ProjectFactory.create_batch(7)
        cls.project: Project = Project.objects.first()

    @classmethod
    def tearDownClass(cls):
        # * ---- Clean execution at the end ----
        super().tearDownClass()
        clean_media_test_folder()

    def test_create_models(self):
        self.assertEqual(Project.objects.count(), 7)

    def test_max_length(self):
        with self.assertRaises(ValidationError) as raised:
            self.project.title = fake_string(256)
            self.project.full_clean()
        raised_msg = raised.exception.message_dict
        self.assertTrue("title" in raised_msg.keys())
        self.assertTrue("at most 255" in raised_msg["title"][0])

    def test_max_file_size(self):
        with self.assertRaises(ValidationError) as raised:
            self.project.cover_image = SimpleUploadedFile(
                name="image.jpg",
                content=fake_image_bytes(9000, 9000),
                content_type="image/jpeg",
            )
            self.project.full_clean()  # noqa
        raised_msg: dict = raised.exception.message_dict
        self.assertTrue("cover_image" in raised_msg.keys())
        self.assertTrue("Max file size" in raised_msg["cover_image"][0])

    def test_auto_generate_webp(self):
        webp_img = self.project.cover_image_webp
        self.assertIsNotNone(webp_img.name)
        Image.open(self.project.cover_image_webp.file)

    def test_auto_generate_slug(self):
        slug = self.project.slug
        self.assertIsNotNone(slug)
        self.assertIsNot("", slug.strip())


class TechnologyModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Initial model objects
        about = AboutFactory.create()
        for _ in range(3):
            tech: Technology = TechnologyFactory.create()
            tech.about.add(about)
            tech.project.add(*ProjectFactory.create_batch(2))
        cls.about = About.objects.first()
        cls.project = Project.objects.first()
        cls.technology = Technology.objects.first()

    @classmethod
    def tearDownClass(cls):
        # * ---- Clean execution at the end ----
        super().tearDownClass()
        clean_media_test_folder()

    def test_create_models(self):
        self.assertEqual(About.objects.count(), 1)
        self.assertEqual(Project.objects.count(), 6)
        self.assertEqual(Technology.objects.count(), 3)

    def test_max_length(self):
        with self.assertRaises(ValidationError) as raised:
            self.technology.name = fake_string(256)
            self.technology.full_clean()
        raised_msg = raised.exception.message_dict
        self.assertTrue("name" in raised_msg.keys())
        self.assertTrue("at most 30" in raised_msg["name"][0])

    def test_max_file_size(self):
        with self.assertRaises(ValidationError) as raised:
            self.technology.logo = SimpleUploadedFile(
                name="image.jpg",
                content=fake_image_bytes(5000, 5000),
                content_type="image/jpeg",
            )
            self.technology.full_clean()  # noqa
        raised_msg: dict = raised.exception.message_dict
        self.assertTrue("logo" in raised_msg.keys())
        self.assertTrue("Max file size" in raised_msg["logo"][0])


class ContactRecordModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Initial model objects
        ContactRecordFactory.create_batch(3)
        cls.contact_record: ContactRecord = ContactRecord.objects.first()

    def test_create_models(self):
        self.assertEqual(ContactRecord.objects.count(), 3)

    def test_max_length(self):
        with self.assertRaises(ValidationError) as raised:
            self.contact_record.name = fake_string(256)
            self.contact_record.email = f"{fake_string(256)}@mail.com"
            self.contact_record.subject = fake_string(256)
            self.contact_record.full_clean()
        raised_msg = raised.exception.message_dict
        self.assertTrue("name" in raised_msg.keys())
        self.assertTrue("at most 255" in raised_msg["name"][0])
        self.assertTrue("email" in raised_msg.keys())
        self.assertTrue("at most 255" in raised_msg["email"][0])
        self.assertTrue("subject" in raised_msg.keys())
        self.assertTrue("at most 255" in raised_msg["subject"][0])
