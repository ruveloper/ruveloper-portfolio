from colorfield.fields import ColorField
from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from solo.models import SingletonModel

from apps.core.utils import upload_cms_image_location
from apps.core.validators import MaxFileSizeValidator, validate_image_logo


class Base(SingletonModel):
    created = models.DateTimeField(_("Created on"), auto_now_add=True)
    modified = models.DateTimeField(_("Modified on"), auto_now=True)

    # * Base data
    email = models.EmailField(_("Email"), max_length=255, help_text=_("Contact email"))
    brand = models.CharField(
        _("Brand"), max_length=255, help_text=_("Name of your personal brand")
    )
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
        help_text=_(
            "Logo of your personal brand. Allow image files (JPG, PNG, GIF, WEBP) + SVG files"
        ),
    )
    favicon = models.ImageField(
        _("favicon"),
        upload_to=upload_cms_image_location,
        validators=[MaxFileSizeValidator(kilobytes=10)],
        help_text=_("Favicon of the website"),
    )

    # * Background colors
    DEFAULT_COLOR_PALETTE = [
        ("#00d3ef", "sky"),
        ("#6eb8f4", "blue"),
        ("#3849ff", "indigo"),
        ("#6427ff", "purple"),
    ]
    color_one = ColorField(
        _("Background Color One"),
        format="hex",
        samples=DEFAULT_COLOR_PALETTE,
        default=DEFAULT_COLOR_PALETTE[0][0],
    )
    color_two = ColorField(
        _("Background Color Two"),
        format="hex",
        samples=DEFAULT_COLOR_PALETTE,
        default=DEFAULT_COLOR_PALETTE[1][0],
    )
    color_three = ColorField(
        _("Background Color Three"),
        format="hex",
        samples=DEFAULT_COLOR_PALETTE,
        default=DEFAULT_COLOR_PALETTE[2][0],
    )
    color_four = ColorField(
        _("Background Color Four"),
        format="hex",
        samples=DEFAULT_COLOR_PALETTE,
        default=DEFAULT_COLOR_PALETTE[3][0],
    )

    # * Social networks
    github = models.URLField(
        _("Github profile url"), help_text=_("Example: https://github.com/dev-user")
    )
    linkedin = models.URLField(
        _("Linkedin profile url"),
        help_text=_("Example: https://www.linkedin.com/in/dev-user"),
    )

    class Meta:
        verbose_name = _("CMS - Base")
        verbose_name_plural = _("CMS - Base")

    def __str__(self):
        return str(_("CMS - Base"))
