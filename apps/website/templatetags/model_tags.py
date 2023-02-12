from django.template import Library

from apps.core.models import TechnologyDescription

register = Library()


@register.filter()
def get_technology_description(queryset, current_language_code) -> str:
    """
    Select the first Technology Description Model that meets the current language code.

    :param <TechnologyDescription QuerySet> queryset
    :param <String> current_language_code
    :rtype: <String> description
    """
    obj: TechnologyDescription = queryset.filter(language=current_language_code).first()
    return obj.description if obj is not None else ""
