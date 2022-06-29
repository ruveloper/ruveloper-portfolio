from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from ckeditor_uploader.fields import RichTextUploadingField
from apps.website.utils import upload_cms_image_location


class Project(models.Model):
    created = models.DateTimeField(_('Created on'), auto_now_add=True)
    modified = models.DateTimeField(_('Modified on'), auto_now=True)

    # ? Project entry data
    title = models.CharField(_('Title'), max_length=255, unique=True)
    cover_image = models.ImageField(_('Cover image'), upload_to=upload_cms_image_location)
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

    class Meta:
        verbose_name = _('CMS - Project')
        verbose_name_plural = _('CMS - Projects')
