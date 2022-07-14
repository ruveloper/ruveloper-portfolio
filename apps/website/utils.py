from io import BytesIO
from pathlib import Path
from typing import Union
from uuid import uuid4

from django.core.files.images import ImageFile
from django.db import models
from django.db.models.fields.files import ImageFieldFile
from django.utils.html import format_html
from PIL import Image


def get_model_or_none(model: type[models.Model]) -> Union[None, type[models.Model]]:
    try:
        return model.objects.get()
    except models.ObjectDoesNotExist:
        return None


# * -------- IMAGE UTILS --------
def upload_cms_image_location(instance, filename: str) -> str:
    extension = filename.split(".")[-1]
    return f"cms/{uuid4().hex}.{extension}"


def convert_img_to_webp(obj: ImageFieldFile) -> ImageFile:
    new_name: str = Path(obj.name).with_suffix(".webp").name
    # Convert image to webp version
    image = Image.open(obj.file)
    webp_image = BytesIO()
    image.save(webp_image, format="webp", optimize=True, quality=90)
    return ImageFile(webp_image, new_name)


def html_img_preview(src_url: str, max_height_px: int = 200):
    if src_url:
        return format_html(
            "<img src='{}' style='width: auto; height: auto; max-height: {}px; object-fit: contain; border-radius: "
            "3px; box-shadow: 0 4px 8px 0 #ccc;'>",
            src_url,
            max_height_px,
        )
    return ""
