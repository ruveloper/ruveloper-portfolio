from django.contrib import admin
from solo.admin import SingletonModelAdmin

from apps.website.models import Base, Home, Project
from apps.website.models import About, Technology, Company, ResumeEntry


# ? --------- Base model ---------
@admin.register(Base)
class BaseAdmin(SingletonModelAdmin): pass


# ? --------- Home model ---------
@admin.register(Home)
class HomeAdmin(SingletonModelAdmin): pass


# ? --------- About model ---------
class TechnologyInline(admin.TabularInline):
    model = Technology
    extra = 0


class CompanyInline(admin.TabularInline):
    model = Company
    extra = 0


class ResumeEntryInline(admin.StackedInline):
    model = ResumeEntry
    extra = 0


@admin.register(About)
class AboutAdmin(SingletonModelAdmin):
    inlines = [TechnologyInline, CompanyInline, ResumeEntryInline]


# ? --------- Project model ---------
admin.site.register(Project)

# ? --------- Shared models ---------
admin.site.register(Technology)
