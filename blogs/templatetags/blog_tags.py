from django import template
from django.conf import settings
register = template.Library()


@register.filter()
def blogs_media_filter(path):
    """
        Фильтрация шаблонных тегов.
        :param path: Путь до изображения
        :return:
    """
    if path:
        return f"{settings.MEDIA_URL}{path}"
    return '#'
