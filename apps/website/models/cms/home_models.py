from django.utils.translation import gettext_lazy as _
from django.db import models

from solo.models import SingletonModel
from apps.website.utils import upload_cms_image_location


class Home(SingletonModel):
    created = models.DateTimeField(_('Created on'), auto_now_add=True)
    modified = models.DateTimeField(_('Modified on'), auto_now=True)

    # ? Card component
    card_title = models.TextField(_('Card title'), blank=True)
    card_body = models.TextField(_('Card Body'), blank=True)

    # ? Developer profile
    dev_photo = models.ImageField(_('Developer photo'), upload_to=upload_cms_image_location, blank=True, null=True)

    class Meta:
        verbose_name = _('CMS - Home')
        verbose_name_plural = _('CMS - Home')

    def __str__(self):
        return str(_('CMS - Home'))
