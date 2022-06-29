from django.db import models
from django.utils.translation import gettext_lazy as _

from solo.models import SingletonModel
from apps.website.utils import upload_cms_image_location


class Base(SingletonModel):
    created = models.DateTimeField(_('Created on'), auto_now_add=True)
    modified = models.DateTimeField(_('Modified on'), auto_now=True)

    # ? Base data
    email = models.EmailField(_('Email'), max_length=255, help_text=_('Contact email'))
    brand = models.CharField(_('Brand'), max_length=255, help_text=_('Name of your personal brand'))
    logo = models.ImageField(
        _('Logo'), upload_to=upload_cms_image_location, help_text=_('Logo of your personal brand')
    )
    favicon = models.ImageField(
        _('favicon'), upload_to=upload_cms_image_location, help_text=_('Favicon of the website')
    )

    # ? Social networks
    github = models.URLField(_('Github profile url'), help_text=_('Example: https://github.com/dev-user'))
    linkedin = models.URLField(_('Linkedin profile url'), help_text=_('Example: https://www.linkedin.com/in/dev-user'))

    class Meta:
        verbose_name = _('CMS - Base')
        verbose_name_plural = _('CMS - Base')

    def __str__(self):
        return str(_('CMS - Base'))
