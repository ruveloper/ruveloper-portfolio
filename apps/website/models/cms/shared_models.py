from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.website.models import About, Project
from apps.website.utils import upload_cms_image_location


class Technology(models.Model):
    created = models.DateTimeField(_('Created on'), auto_now_add=True)
    modified = models.DateTimeField(_('Modified on'), auto_now=True)

    # ? Relations
    about = models.ForeignKey(About, null=True, on_delete=models.SET_NULL)
    project_entry = models.ForeignKey(Project, null=True, on_delete=models.SET_NULL)

    # ? Technology data
    name = models.CharField(_('Name'), max_length=30, unique=True)
    logo = models.ImageField(_('Logo'), upload_to=upload_cms_image_location, blank=True, null=True)
    description = models.TextField(_('Description'), blank=True)

    # ? Extra options
    priority_order = models.PositiveSmallIntegerField(
        _('Priority order'), default=0,
        help_text=_('Positive number used to order, the highest number is positioned first.')
    )

    class Meta:
        verbose_name = _('CMS - Technology')
        verbose_name_plural = _('CMS - Technologies')
        ordering = ['priority_order']

    def __str__(self):
        return self.name
