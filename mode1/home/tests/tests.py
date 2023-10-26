from django.test import TestCase
from home.models import Product


class TestMode(TestCase):
    def test_mode(self):
        product = Product.objects.create(name='iphone',price=10000)
        self.assertTrue(isinstance(product,Product))
        self.assertEquals(str(product),'iphone')
        print("isinstance:",isinstance(product,Product))

