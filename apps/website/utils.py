from typing import Type, Union
from uuid import uuid4

from django.db import models
from solo.models import SingletonModel


def get_model_or_none(model: Type[models.Model]) -> Union[None, Type[models.Model]]:
    try:
        return model.objects.get()
    except models.ObjectDoesNotExist:
        return None


def upload_cms_image_location(instance, filename: str) -> str:
    extension = filename.split('.')[-1]
    return f'cms/{uuid4().hex}.{extension}'
