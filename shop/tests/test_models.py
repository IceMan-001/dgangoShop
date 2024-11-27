from django.test import TestCase
from shop.models import Category

class CategoryModelTestCase(TestCase):
    def setUp(self):
        Category.objects.create(name='Phones', slug='phones')

    def test_categories_name(self):
        phone = Category.objects.get(name='Phones')
        self.assertEqual(phone.name, 'Phones')

    def test_categories_slug(self):
        phone = Category.objects.get(name='phones')
        self.assertEqual(phone.slug, 'phones')