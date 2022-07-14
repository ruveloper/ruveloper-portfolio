from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from solo.models import SingletonModel

from apps.core.utils import convert_img_to_webp, upload_cms_image_location
from apps.core.validators import MaxFileSizeValidator


class Home(SingletonModel):
    created = models.DateTimeField(_("Created on"), auto_now_add=True)
    modified = models.DateTimeField(_("Modified on"), auto_now=True)

    # * Card component
    card_title = models.TextField(_("Card title"), blank=True)
    card_body = models.TextField(_("Card Body"), blank=True)

    # * Developer
    dev_photo = models.ImageField(
        _("Developer photo"),
        blank=True,
        null=True,
        upload_to=upload_cms_image_location,
        validators=[
            FileExtensionValidator(allowed_extensions=["jpg", "jpeg", "png"]),
            MaxFileSizeValidator(kilobytes=1000),
        ],
    )
    dev_photo_webp = models.ImageField(
        _("Developer photo (Webp)"),
        blank=True,
        null=True,
        editable=False,
        upload_to=upload_cms_image_location,
        help_text=_("Auto-generated WEBP version of [Developer photo]"),
    )

    def save(self, *args, **kwargs):
        # * ---- Before save model ----
        # Auto-generate webp version of image field for web optimizations
        self.dev_photo_webp = (
            convert_img_to_webp(self.dev_photo) if bool(self.dev_photo.name) else None
        )

        super().save(*args, **kwargs)
        return

    class Meta:
        verbose_name = _("CMS - Home")
        verbose_name_plural = _("CMS - Home")

    def __str__(self):
        return str(_("CMS - Home"))
