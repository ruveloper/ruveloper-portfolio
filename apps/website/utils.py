from uuid import uuid4


def upload_cms_image_location(instance, filename:str):
    extension = filename.split('.')[-1]
    return f'cms/{uuid4().hex}.{extension}'




