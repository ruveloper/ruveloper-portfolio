from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from django.core.validators import FileExtensionValidator

from ckeditor_uploader.fields import RichTextUploadingField
from apps.website.utils import upload_cms_image_location, convert_img_to_webp


class Project(models.Model):
    created = models.DateTimeField(_('Created on'), auto_now_add=True)
    modified = models.DateTimeField(_('Modified on'), auto_now=True)

    # ? Project entry data
    title = models.CharField(_('Title'), max_length=255, unique=True)
    cover_image = models.ImageField(
        _('Cover image'), blank=True, null=True,
        upload_to=upload_cms_image_location,
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])]
    )
    cover_image_webp = models.ImageField(
        _('Cover image (Webp)'), blank=True, null=True, editable=False,
        upload_to=upload_cms_image_location,
        help_text=_('Auto-generated WEBP version of [Cover image]')
    )
    description = models.TextField(_('Description'))

    # ? Project details
    slug = models.SlugField(
        _('Slug'), max_length=255, unique=True, blank=True,
        help_text=_('Url endpoint of this project, leave blank to auto-generate.')
    )
    detail = RichTextUploadingField(
        _('Project details'),
        help_text=_('Long description about the project, it is the content of the project endpoint')
    )

    def get_absolute_url(self):
        return reverse("website:project_detail", kwargs={'project_slug': self.slug})

    def save(self, *args, **kwargs):
        # * ---- Before save model ----
        # Auto-generate webp version of image field for web optimizations
        self.cover_image_webp = convert_img_to_webp(self.cover_image) if bool(self.cover_image.name) else None

        super(Project, self).save(*args, **kwargs)
        return

    class Meta:
        verbose_name = _('CMS - Project')
        verbose_name_plural = _('CMS - Projects')
