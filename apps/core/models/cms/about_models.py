from django.conf import settings
from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.core.utils import convert_img_to_webp, upload_cms_image_location
from apps.core.validators import MaxFileSizeValidator, validate_image_logo


class About(models.Model):
    created = models.DateTimeField(_("Created on"), auto_now_add=True)
    modified = models.DateTimeField(_("Modified on"), auto_now=True)

    # * Language selector
    language = models.CharField(
        _("Language"),
        max_length=30,
        choices=settings.LANGUAGES,
        default=settings.LANGUAGE_CODE,
    )

    # * Profile section
    profile_image = models.ImageField(
        _("Profile image"),
        blank=True,
        null=True,
        upload_to=upload_cms_image_location,
        validators=[
            FileExtensionValidator(allowed_extensions=["jpg", "jpeg", "png"]),
            MaxFileSizeValidator(kilobytes=1000),
        ],
    )
    profile_image_webp = models.ImageField(
        _("Profile image (Webp)"),
        blank=True,
        null=True,
        editable=False,
        upload_to=upload_cms_image_location,
        help_text=_("Auto-generated WEBP version of [Profile image]"),
    )
    body = models.TextField(_("Profile body"))

    # * Activate/Deactivate Optional sections
    activate_stack = models.BooleanField(_("Activate stack section"), default=True)
    activate_trust_me = models.BooleanField(
        _("Activate trust me section"), default=True
    )
    activate_resume = models.BooleanField(_("Activate resume section"), default=True)

    def save(self, *args, **kwargs):
        # * ---- Before save model ----
        # Auto-generate webp version of image field for web optimizations
        self.profile_image_webp = (
            convert_img_to_webp(self.profile_image)
            if bool(self.profile_image.name)
            else None
        )

        super().save(*args, **kwargs)
        return

    class Meta:
        verbose_name = _("CMS - About")
        verbose_name_plural = _("CMS - About")
        ordering = ["language", "-modified"]

    def __str__(self):
        return str(_("CMS - About"))


class Company(models.Model):
    created = models.DateTimeField(_("Created on"), auto_now_add=True)
    modified = models.DateTimeField(_("Modified on"), auto_now=True)

    # * Relations
    about = models.ForeignKey(About, on_delete=models.CASCADE)

    # * Company data
    name = models.CharField(_("Name"), max_length=255, unique=True)
    logo = models.FileField(
        _("Logo"),
        upload_to=upload_cms_image_location,
        validators=[
            FileExtensionValidator(
                allowed_extensions=["jpg", "jpeg", "png", "gif", "webp", "svg"]
            ),
            MaxFileSizeValidator(kilobytes=100),
            validate_image_logo,
        ],
        help_text=_("Allow image files (JPG, PNG, GIF, WEBP) + SVG files"),
    )

    # * Extra options
    priority_order = models.PositiveSmallIntegerField(
        _("Priority order"),
        default=0,
        help_text=_(
            "Positive number used to order, the highest number is positioned first."
        ),
    )

    class Meta:
        verbose_name = _("Company")
        verbose_name_plural = _("Companies")
        ordering = ["-priority_order"]

    def __str__(self):
        return self.name


class ResumeEntry(models.Model):
    created = models.DateTimeField(_("Created on"), auto_now_add=True)
    modified = models.DateTimeField(_("Modified on"), auto_now=True)

    # * Relations
    about = models.ForeignKey(About, on_delete=models.CASCADE)

    # * Resume entry data
    title = models.CharField(_("Title"), max_length=255)
    company = models.CharField(_("Company or institution"), max_length=255)
    start = models.DateField(_("Start date"))
    end = models.DateField(_("End date"), blank=True, null=True)
    description = models.TextField(_("Description"), blank=True)

    # * Type of entry
    class EntryTypes(models.TextChoices):
        EXPERIENCE = "Experience", _("Experience")
        EDUCATION = "Education", _("Education")

    type = models.CharField(
        _("Type of entry"),
        max_length=10,
        choices=EntryTypes.choices,
        default=EntryTypes.EXPERIENCE,
    )

    # * Extra options
    priority_order = models.PositiveSmallIntegerField(
        _("Priority order"),
        default=0,
        help_text=_(
            "Positive number used to order, the highest number is positioned first."
        ),
    )

    class Meta:
        verbose_name = _("Resume entry")
        verbose_name_plural = _("Resume entries")
        ordering = ["-priority_order"]

    def __str__(self):
        return self.title
