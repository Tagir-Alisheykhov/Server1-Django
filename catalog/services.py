from django.core.cache import cache

from config.settings import CACHE_ENABLED
from .models import Product


def get_products_from_cache():
    """
        Получение списка товаров из кэша.
        Если кэш пуст, то получаем данные из БД.
    """
    if not CACHE_ENABLED:
        return Product.objects.all()
    else:
        key = "products_list"
        products = cache.get(key)
        if products is not None:
            return products
        else:
            products = Product.objects.all()
            cache.set(key, products, timeout=60)
            return products


def get_products_by_category(cached_products, category_slug=None):
    """ Получение списка товаров в указанной категории """
    if not category_slug:
        print("Нет category_slug")
        return cached_products
    else:
        print("Есть category_slug")
        return [
            product for product in cached_products
            if product.category.slug == category_slug
        ]
