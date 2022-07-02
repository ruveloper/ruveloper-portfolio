from io import BytesIO
from uuid import uuid4
from PIL import Image
from pathlib import Path
from typing import Type, Union

from django.db import models
from django.db.models.fields.files import ImageFieldFile
from django.core.files.images import ImageFile


def get_model_or_none(model: Type[models.Model]) -> Union[None, Type[models.Model]]:
    try:
        return model.objects.get()
    except models.ObjectDoesNotExist:
        return None


# * -------- IMAGE UTILS --------
def upload_cms_image_location(instance, filename: str) -> str:
    extension = filename.split('.')[-1]
    return f'cms/{uuid4().hex}.{extension}'


def convert_img_to_webp(obj: ImageFieldFile) -> ImageFile:
    new_name: str = Path(obj.name).with_suffix('.webp').name
    # Convert image to webp version
    image = Image.open(obj.file)
    webp_image = BytesIO()
    image.save(webp_image, format='webp', optimize=True, quality=90)
    return ImageFile(webp_image, new_name)
