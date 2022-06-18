from django.conf import settings
from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.core.models import About, Project
from apps.core.utils import upload_cms_image_location
from apps.core.validators import MaxFileSizeValidator


class Technology(models.Model):
    created = models.DateTimeField(_("Created on"), auto_now_add=True)
    modified = models.DateTimeField(_("Modified on"), auto_now=True)

    # * Language selector
    language = models.CharField(
        _("Language"),
        max_length=30,
        choices=settings.LANGUAGES,
        default=settings.LANGUAGE_CODE,
    )

    # * Relations
    about = models.ManyToManyField(About, blank=True)
    project = models.ManyToManyField(Project, blank=True)

    # * Technology data
    name = models.CharField(_("Name"), max_length=30)
    logo = models.FileField(
        _("Logo"),
        upload_to=upload_cms_image_location,
        validators=[
            FileExtensionValidator(
                allowed_extensions=["jpg", "jpeg", "png", "gif", "webp", "svg"]
            ),
            MaxFileSizeValidator(kilobytes=100),
        ],
        help_text=_("Allow image files (JPG, PNG, GIF, WEBP) + SVG files"),
    )
    description = models.TextField(_("Description"), blank=True)

    # * Extra options
    priority_order = models.PositiveSmallIntegerField(
        _("Priority order"),
        default=0,
        help_text=_(
            "Positive number used to order, the highest number is positioned first."
        ),
    )

    class Meta:
        verbose_name = _("CMS - Technology")
        verbose_name_plural = _("CMS - Technologies")
        ordering = ["language", "-priority_order"]

    def __str__(self):
        return f"{self.language}: {self.name}"
