from pathlib import Path
from typing import Union

from django.core.exceptions import ValidationError
from django.db.models.fields.files import FieldFile, ImageFieldFile
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _
from PIL import Image


def validate_image_logo(obj: FieldFile):
    """
    Validate the content of uploaded image except SVG (it's a vector-based format)
    :param obj:
    :raises ValidationError: If the content is not valid or corrupt
    """
    img = obj.file
    img_extension: str = Path(img.name).suffix
    if img_extension != ".svg":
        try:
            Image.open(img.file)
        except OSError:
            raise ValidationError(_("The image file is invalid or corrupt"))


@deconstructible
class MaxFileSizeValidator:
    """
    Validate the max size for the uploaded file
    :param kilobytes: Optional; maximum file size in KB (Default: 500 KB).
    :param message: Optional; custom message.
    :raises ValidationError: If the file size is greater than [kilobytes]
    """

    message = _(
        "File size %(file_size).2f KB is not allowed. "
        "Max file size is: %(kilobytes).2f KB."
    )
    kilobytes: float = 500.0

    def __init__(self, kilobytes: float = None, message: str = None):
        if kilobytes is not None:
            self.kilobytes = float(kilobytes)
        if message is not None:
            self.message = message

    def __call__(self, obj: Union[FieldFile, ImageFieldFile]):
        file_size: float = obj.size / 1000  # In Kilobytes
        if file_size > self.kilobytes:
            raise ValidationError(
                self.message,
                params={
                    "file_size": file_size,
                    "kilobytes": self.kilobytes,
                },
            )
