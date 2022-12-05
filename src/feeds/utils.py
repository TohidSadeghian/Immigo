from os import path
from django.core.exceptions import ValidationError
from django.utils import timezone


def is_image(ext):
    support_ext = ['jpeg', 'jpg', 'png', 'bmp' ,'webp']
    if ext.lower() not in support_ext:
        raise ValidationError('unknown file format')
    return True

def news_image(instance, filename):
    ext = filename.split('.')[-1].lower()
    if is_image(ext):
        return path.join('.', 'img', 'news_image', '{}.{}'.format(int(timezone.now().timestamp()), ext))
