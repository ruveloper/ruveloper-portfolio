from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from apps.website.utils import html_img_preview


def get_technology_inline(_model):
    class TechnologyInline(admin.TabularInline):
        model = _model
        extra = 0
        verbose_name = _("Technology")
        verbose_name_plural = _("Technologies")

        # * Extra inline fields
        readonly_fields = ("logo_preview",)

        @staticmethod
        @admin.display(description=_("Logo preview"))
        def logo_preview(instance):
            return html_img_preview(
                src_url=instance.technology.logo.url, max_height_px=30
            )

    return TechnologyInline
