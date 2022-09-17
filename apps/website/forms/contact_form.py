from django import forms
from django.conf import settings
from django.core.mail import send_mail
from django.utils.translation import gettext_lazy as _

from apps.core.models import ContactRecord


class ContactRecordForm(forms.ModelForm):
    def send_email(self):
        data = self.cleaned_data
        msg = f'{_("Name")}: {data["name"]}\n'
        msg += f'{_("Email")}: {data["email"]}\n'
        msg += f'{_("Subject")}: {data["subject"]}\n\n'
        msg += f'{_("Say")}: {data["message"]}\n\n'
        # ! Send email to SMTP server
        send_mail(
            subject=f'[{_("Form contact")}] {data["email"]}',
            message=msg,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=settings.RECIPIENT_ADDRESS,
            fail_silently=not settings.DEBUG,  # If DEBUG True, fail_silently False
        )

    class Meta:
        model = ContactRecord
        fields = ["name", "email", "subject", "message"]
        exclude = ["created", "modified"]
