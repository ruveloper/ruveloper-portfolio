from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from solo.admin import SingletonModelAdmin

from apps.core.admin.shared_admin import get_technology_inline
from apps.core.models import (
    About,
    Base,
    Company,
    Home,
    Project,
    ResumeEntry,
    Technology,
)
from apps.core.utils import html_img_preview


# * ------------------ Base model ------------------
@admin.register(Base)
class BaseAdmin(SingletonModelAdmin):
    readonly_fields = ("logo_preview", "favicon_preview")
    fieldsets = [
        (None, {"fields": ["email"]}),
        (
            _("Personal brand"),
            {"fields": ["brand", "logo", "logo_preview", "favicon", "favicon_preview"]},
        ),
        (_("Social networks"), {"fields": ["github", "linkedin"]}),
    ]

    # * Image previews
    @staticmethod
    @admin.display(description=_("Logo preview"))
    def logo_preview(self):
        return html_img_preview(src_url=self.logo.url, max_height_px=100)

    @staticmethod
    @admin.display(description=_("Favicon preview"))
    def favicon_preview(self):
        return html_img_preview(src_url=self.favicon.url, max_height_px=100)


# * ------------------ Home model ------------------
@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    readonly_fields = ("id", "dev_photo_webp", "dev_photo_preview")
    list_display = ("__str__", "id", "language")
    fieldsets = [
        (
            None,
            {
                "fields": [
                    ("id", "language"),
                    "dev_photo",
                    "dev_photo_webp",
                    "dev_photo_preview",
                ]
            },
        ),
        (_("Card"), {"fields": ["card_title", "card_body"]}),
    ]

    # * Image preview
    @staticmethod
    @admin.display(description=_("Developer photo preview"))
    def dev_photo_preview(obj: Home):
        return html_img_preview(src_url=obj.dev_photo.url)


# * ------------------ About model ------------------
class CompanyInline(admin.TabularInline):
    model = Company
    extra = 0

    # * Extra inline fields
    readonly_fields = ("logo_preview",)

    @staticmethod
    @admin.display(description=_("Logo preview"))
    def logo_preview(obj: Company):
        return html_img_preview(src_url=obj.logo.url, max_height_px=30)


class ResumeEntryInline(admin.StackedInline):
    model = ResumeEntry
    extra = 0
    fields = [
        "title",
        "company",
        "start",
        "end",
        "type",
        "priority_order",
        "description",
    ]


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    readonly_fields = ("id", "profile_image_webp", "profile_image_preview")
    list_display = ("__str__", "id", "language")
    fieldsets = [
        (None, {"fields": [("id", "language")]}),
        (
            _("Profile"),
            {
                "fields": [
                    "profile_image",
                    "profile_image_webp",
                    "profile_image_preview",
                    "body",
                ]
            },
        ),
        (
            _("Activate/Inactivate sections"),
            {"fields": ["activate_stack", "activate_trust_me", "activate_resume"]},
        ),
    ]
    # Inline ManyToMany Relation managed by the through attribute (the intermediary model)
    inlines = [
        get_technology_inline(Technology.about.through),
        CompanyInline,
        ResumeEntryInline,
    ]

    # * Image preview
    @staticmethod
    @admin.display(description=_("Profile image preview"))
    def profile_image_preview(self):
        return html_img_preview(src_url=self.profile_image.url)


# * ------------------ Project model ------------------
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = (
        "id",
        "cover_image_webp",
        "cover_image_preview",
        "mini_cover_image_preview",
    )
    list_display = ("title", "language", "priority_order", "mini_cover_image_preview")
    fieldsets = [
        (
            None,
            {
                "fields": [
                    ("id", "language"),
                    "title",
                    "slug",
                    "priority_order",
                    "cover_image",
                    "cover_image_webp",
                    "cover_image_preview",
                ]
            },
        ),
        (_("Project content"), {"fields": ["description", "detail"]}),
    ]
    # Inline ManyToMany Relation managed by the through attribute (the intermediary model)
    inlines = [
        get_technology_inline(Technology.project.through),
    ]

    # * Image preview
    @staticmethod
    @admin.display(description=_("Cover image preview"))
    def cover_image_preview(obj: Project):
        return html_img_preview(src_url=obj.cover_image.url)

    @staticmethod
    @admin.display(description=_("Cover image preview"))
    def mini_cover_image_preview(obj: Project):
        return html_img_preview(src_url=obj.cover_image.url, max_height_px=50)


# * ------------------ Shared models ------------------
@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    readonly_fields = ("id", "logo_preview", "mini_logo_preview")
    list_display = ("name", "language", "priority_order", "mini_logo_preview")
    filter_horizontal = ("project", "about")
    fieldsets = [
        (
            None,
            {
                "fields": [
                    ("id", "language"),
                    "name",
                    "priority_order",
                    "logo",
                    "logo_preview",
                    "description",
                ]
            },
        ),
    ]

    # * Image preview
    @staticmethod
    @admin.display(description=_("Logo preview"))
    def logo_preview(obj: Technology):
        return html_img_preview(src_url=obj.logo.url, max_height_px=100)

    @staticmethod
    @admin.display(description=_("Logo preview"))
    def mini_logo_preview(obj: Technology):
        return html_img_preview(src_url=obj.logo.url, max_height_px=20)
