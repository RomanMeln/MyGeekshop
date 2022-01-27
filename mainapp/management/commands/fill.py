import json

from django.conf import settings

from django.core.management import BaseCommand
from mainapp.models import ProductCategory, Product

from authapp.models import ShopUser


def load_from_json(file_name):
    with open(f'{settings.BASE_DIR}/json/{file_name}.json', 'r', encoding='utf-8') as json_file:
        return json.load(json_file)


class Command(BaseCommand):

    def handle(self, *args, **options):
        categories = load_from_json('categories')
        ProductCategory.objects.all().delete()
        for category in categories:
            new_category = ProductCategory(**category)
            new_category.save()

        products = load_from_json('products')
        Product.objects.all().delete()
        for prod in products:
            category_name = prod["category"]
            _category = ProductCategory.objects.get(name=category_name)
            prod['category'] = _category
            new_product = Product(**prod)
            new_product.save()

        shop_admin = ShopUser.objects.create_superuser(
            username='django',
            password='geekbrains',
            email='django@geekshop.local'
        )
