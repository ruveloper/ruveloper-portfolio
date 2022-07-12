from django.contrib import admin

from apps.website.models import ContactRecord


# * --------------- Contact Record model ------------------
@admin.register(ContactRecord)
class ContactRecordAdmin(admin.ModelAdmin):
    readonly_fields = ('name', 'email', 'subject', 'message')
    list_display = ['__str__', 'created', 'name', 'email', 'subject']

    # * ---- Permissions ----
    def has_add_permission(self, request): return False

    def has_change_permission(self, request, obj=None): return False
