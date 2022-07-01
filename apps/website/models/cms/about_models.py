from django.db import models
from django.utils.translation import gettext_lazy as _

from django.core.validators import FileExtensionValidator
from apps.website.validators import validate_image_logo

from solo.models import SingletonModel
from apps.website.utils import upload_cms_image_location


class About(SingletonModel):
    created = models.DateTimeField(_('Created on'), auto_now_add=True)
    modified = models.DateTimeField(_('Modified on'), auto_now=True)

    # ? Profile section
    image = models.ImageField(_('Profile image'), upload_to=upload_cms_image_location, blank=True, null=True)
    body = models.TextField(_('Profile body'))

    # ? Activate/Deactivate Optional sections
    activate_stack = models.BooleanField(_('Activate stack section'), default=True)
    activate_trust_me = models.BooleanField(_('Activate trust me section'), default=True)
    activate_resume = models.BooleanField(_('Activate resume section'), default=True)

    class Meta:
        verbose_name = _('CMS - About')

    def __str__(self):
        return str(_('CMS - About'))


class Company(models.Model):
    created = models.DateTimeField(_('Created on'), auto_now_add=True)
    modified = models.DateTimeField(_('Modified on'), auto_now=True)

    # ? Relations
    about = models.ForeignKey(About, on_delete=models.CASCADE)

    # ? Company data
    name = models.CharField(_('Name'), max_length=255, unique=True)
    logo = models.FileField(
        _('Logo'), upload_to=upload_cms_image_location,
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'gif', 'webp', 'svg']),
                    validate_image_logo],
        help_text=_('Allow image files (JPG, PNG, GIF, WEBP) + SVG files')
    )

    # ? Priority order
    priority_order = models.PositiveSmallIntegerField(
        _('Priority order'), default=0,
        help_text=_('Positive number used to order, the highest number is positioned first.')
    )

    class Meta:
        verbose_name = _('Company')
        verbose_name_plural = _('Companies')

    def __str__(self):
        return self.name


class ResumeEntry(models.Model):
    created = models.DateTimeField(_('Created on'), auto_now_add=True)
    modified = models.DateTimeField(_('Modified on'), auto_now=True)

    # ? Relations
    about = models.ForeignKey(About, on_delete=models.CASCADE)

    # ? Resume entry data
    title = models.CharField(_('Title'), max_length=255)
    start = models.DateField(_('Start date'))
    end = models.DateField(_('End date'), blank=True, null=True)
    description = models.TextField(_('Description'), blank=True)

    # ? Type of entry
    class EntryTypes(models.TextChoices):
        EXPERIENCE = 'Experience', _('Experience')
        EDUCATION = 'Education', _('Education')

    type = models.CharField(
        _('Type of entry'), max_length=10,
        choices=EntryTypes.choices, default=EntryTypes.EXPERIENCE
    )

    class Meta:
        verbose_name = _('Resume entry')
        verbose_name_plural = _('Resume entries')
        ordering = ['-start']

    def __str__(self):
        return self.title
