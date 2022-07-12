from django.db import models
from django.utils.translation import gettext_lazy as _


class ContactRecord(models.Model):
    created = models.DateTimeField(_('Created on'), auto_now_add=True)
    modified = models.DateTimeField(_('Modified on'), auto_now=True)

    # * Contact record data
    name = models.CharField(_('Name'), max_length=255, blank=True)
    email = models.EmailField(_('Email'), max_length=255)
    subject = models.CharField(_('Subject'), max_length=255, blank=True)
    message = models.TextField(_('Message'))

    class Meta:
        verbose_name = _('Contact record')
        verbose_name_plural = _('Contact records')
        ordering = ['-created']

    def __str__(self):
        return f'{_("Record")} {self.id}'
