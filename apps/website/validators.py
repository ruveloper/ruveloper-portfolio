from pathlib import Path
from PIL import Image
from django.db.models.fields.files import FieldFile
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_image_logo(obj: FieldFile):
    img = obj.file
    img_extension:str = Path(img.name).suffix
    # Validate img file except SVG (it's a vector)
    if img_extension != '.svg':
        try:
            Image.open(img.file)
        except IOError:
            raise ValidationError(_('The image file is invalid or corrupt'))
