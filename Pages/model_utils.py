from PIL import Image
from io import BytesIO


def compress_image(image):
    img = Image.open(image.path)
    _byte = BytesIO()
    img.save(_byte, format="JPEG", quality=75)
    return _byte
