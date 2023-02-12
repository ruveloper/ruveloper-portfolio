from django.conf import settings
from django.core.validators import FileExtensionValidator
from django.db import models
from django.urls import reverse
from django.utils.text import Truncator, slugify
from django.utils.translation import gettext_lazy as _
from tinymce.models import HTMLField

from apps.core.utils import convert_img_to_webp, upload_cms_image_location
from apps.core.validators import MaxFileSizeValidator


class Project(models.Model):
    created = models.DateTimeField(_("Created on"), auto_now_add=True)
    modified = models.DateTimeField(_("Modified on"), auto_now=True)

    # * Language selector
    language = models.CharField(
        _("Language"),
        max_length=30,
        choices=settings.LANGUAGES,
        default=settings.LANGUAGE_CODE,
    )

    # * Project entry data
    title = models.CharField(_("Title"), max_length=255)
    slug = models.SlugField(
        _("Slug"),
        max_length=255,
        blank=True,
        help_text=_(
            "Url endpoint for this project, leave blank to auto-generate. <br>"
            "<strong>WARNING:</strong> Set the same slug for the project model in different languages."
        ),
    )
    link = models.URLField(
        _("Website URL or link to project demo"),
        blank=True,
        null=True,
        help_text=_(
            "Link to deployed project. Leave this field blank to hide the corresponding button on the projects page."
        ),
    )
    github_url = models.URLField(
        _("Github repository URL"),
        blank=True,
        null=True,
        help_text=_(
            "Link to project code repository. "
            "leave this field blank to hide the corresponding button on the projects page."
        ),
    )
    cover_image = models.ImageField(
        _("Cover image"),
        blank=True,
        null=True,
        upload_to=upload_cms_image_location,
        validators=[
            FileExtensionValidator(allowed_extensions=["jpg", "jpeg", "png"]),
            MaxFileSizeValidator(kilobytes=1000),
        ],
    )
    cover_image_webp = models.ImageField(
        _("Cover image (Webp)"),
        blank=True,
        null=True,
        editable=False,
        upload_to=upload_cms_image_location,
        help_text=_("Auto-generated WEBP version of [Cover image]."),
    )
    description = models.TextField(
        _("Description"),
        help_text=_("< Accept HTML > Project summary to display in project list."),
    )

    # * Project details
    activate_details = models.BooleanField(
        _("Activate project details"),
        default=True,
        help_text=_("Activate project details button and expose project details page"),
    )
    detail = HTMLField(
        _("Project details"),
        blank=True,
        null=True,
        help_text=_(
            "< Accept HTML > Long description about the project, it's the content of the project details page."
        ),
    )

    # * Extra options
    priority_order = models.PositiveSmallIntegerField(
        _("Priority order"),
        default=0,
        help_text=_(
            "Positive number used to order, the highest number is positioned first."
        ),
    )

    def get_absolute_url(self):
        return reverse("website:project_detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        # * ---- Before save model ----
        # Auto-generate webp version of image field for web optimizations
        self.cover_image_webp = (
            convert_img_to_webp(self.cover_image)
            if bool(self.cover_image.name)
            else None
        )
        # Auto-generate slug if isn't set
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        return

    class Meta:
        verbose_name = _("CMS - Project")
        verbose_name_plural = _("CMS - Projects")
        ordering = ["slug", "language", "-priority_order"]

    def __str__(self):
        return Truncator(f'{self.language}: {_("Project")} {self.title}').chars(
            50, truncate="..."
        )
