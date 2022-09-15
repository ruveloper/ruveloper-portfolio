import io
import os
import random
import shutil
import string

from PIL import Image


def fake_string(length: int = 10) -> str:
    """
    Create a fake string with the specified length
    :param length: (int)
    :return: (str)
    """
    chars = string.ascii_lowercase + string.ascii_uppercase + string.digits
    return "".join(random.choice(chars) for _ in range(length))


def fake_file_bytes(kb_size: int = 100) -> bytes:
    """
    Create random bytes with the specified size that we can use in fake files
    :param kb_size: Size in Kilo Bytes, Default: 100 KB.
    :return: (bytes)
    """
    return random.randbytes(kb_size * 1024)


def fake_image_bytes(width: int = 100, height: int = 100, img_format="jpeg") -> bytes:
    """
    Create image valid random bytes with the specified size
    :param width: (int)
    :param height: (int)
    :param img_format: (str)
    :return: (bytes) valid image bytes
    """
    img_b = io.BytesIO()
    img = Image.new(mode="RGB", size=(width, height), color="indigo")
    img.save(img_b, format=img_format)
    return img_b.getvalue()


def clean_media_test_folder() -> None:
    """
    Clen media folder used in tests.
    """
    if os.path.exists("./media_test"):
        shutil.rmtree("./media_test", ignore_errors=True)
