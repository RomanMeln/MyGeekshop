from django import template
from django.conf import settings


register = template.Library()


@register.filter(name='media_for_users')
def media_for_users(avatar):

    if not avatar:
        avatar = 'search-1.png'

    return f'{settings.MEDIA_URL}{avatar}'


def media_for_products(image):
    """
    Автоматически добавляет относительный URL-путь к медиафайлам продуктов
    products_images/product1.jpg --> /media/products_images/product1.jpg
    """
    if not image:
        image = 'products_images/search.png'

    return f'{settings.MEDIA_URL}{image}'


register.filter('media_for_products', media_for_products)
