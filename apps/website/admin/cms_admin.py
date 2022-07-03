from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from solo.admin import SingletonModelAdmin
from apps.website.models import Base, Home, Project
from apps.website.models import About, Technology, Company, ResumeEntry


# ? --------- Base model ---------
@admin.register(Base)
class BaseAdmin(SingletonModelAdmin):
    fieldsets = [
        (None, {'fields':['email']}),
        (_('Personal brand'), {'fields':['brand', 'logo', 'favicon']}),
        (_('Social networks'), {'fields':['github', 'linkedin']})
    ]


# ? --------- Home model ---------
@admin.register(Home)
class HomeAdmin(SingletonModelAdmin):
    readonly_fields = ('dev_photo_webp',)
    fieldsets = [
        (None, {'fields':['dev_photo', 'dev_photo_webp']}),
        (_('Card'), {'fields':['card_title', 'card_body']}),
    ]


# ? --------- About model ---------
class TechnologyAboutInline(admin.TabularInline):
    # ManyToMany Relation managed by the through attribute
    model = Technology.about.through
    extra = 0


class CompanyInline(admin.TabularInline):
    model = Company
    extra = 0


class ResumeEntryInline(admin.StackedInline):
    model = ResumeEntry
    extra = 0


@admin.register(About)
class AboutAdmin(SingletonModelAdmin):
    readonly_fields = ('profile_image_webp',)
    fieldsets = [
        (_('Profile'), {'fields':['profile_image', 'profile_image_webp', 'body']}),
        (_('Activate/Inactivate sections'), {'fields':['activate_stack', 'activate_trust_me', 'activate_resume']})
    ]
    inlines = [TechnologyAboutInline, CompanyInline, ResumeEntryInline]


# ? --------- Project model ---------
class TechnologyProjectInline(admin.TabularInline):
    model = Technology.project.through
    extra = 0


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('cover_image_webp',)
    fieldsets = [
        (None, {'fields':['title', 'slug', 'cover_image', 'cover_image_webp']}),
        (_('Project content'), {'fields':['description', 'detail']})
    ]
    inlines = [TechnologyProjectInline, ]


# ? --------- Shared models ---------
@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    filter_horizontal = ('project', 'about')
    fieldsets = [
        (None, {'fields':['name', 'logo', 'priority_order', 'description']}),
    ]
