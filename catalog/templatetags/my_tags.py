from django import template

register = template.Library()


@register.filter()
def media_filter(path):
    """
        Фильтрация шаблонных тегов.
        :param path: Путь до изображения
        :return:
    """
    if path:
        return f"/media/{path}"
    return '#'
