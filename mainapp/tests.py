from django.test import TestCase
from mainapp.models import Product, ProductCategory


class TestMainappSmoke(TestCase):
    def setUp(self) -> None:
        category = ProductCategory.objects.create(
            name='cat1'
        )
        for i in range(10):
            Product.objects.create(
                category=category,
                name=f'prod#{i}',
                description='test'
            )

    def test_mainapp_urls(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_categories_urls(self):
        for category in ProductCategory.objects.all():
            response = self.client.get(f'/products/{category.pk}/')
            self.assertEqual(response.status_code, 200)

    def test_products_urls(self):
        for product in Product.objects.all():
            response = self.client.get(f'/products/product/{product.pk}/')
            self.assertEqual(response.status_code, 200)
