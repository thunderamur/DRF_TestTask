from django.test import TestCase

from mixer.backend.django import mixer

from mainapp.models import Company, Product, Price


class PriceModelTestCase(TestCase):
    def setUp(self):
        self.price_price = 100.50
        self.product_name = 'Product'
        self.company_name = 'Company'
        self.product = mixer.blend(Product, name=self.product_name)
        self.company = mixer.blend(Company, name=self.company_name)
        self.price = mixer.blend(Price, price=self.price_price, product=self.product, company=self.company)

    def test_str(self):
        expected = f'{self.price_price} ({self.product_name} ({self.company_name}))'
        result = str(self.price)
        self.assertEqual(expected, result)
