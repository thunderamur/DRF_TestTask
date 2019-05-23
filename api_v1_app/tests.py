from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from mixer.backend.django import mixer

from mainapp.models import District, Company, Product, Price


class ProductAPITestCase(APITestCase):
    def setUp(self):
        self.product = mixer.blend(Product)

    def test_retrieve(self):
        url = reverse('api_v1_app:product-detail', args=(self.product.pk,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.product.name)


class CompanyAPITestCase(APITestCase):
    def setUp(self):
        self.district = mixer.blend(District)
        self.company = mixer.blend(Company, districts=self.district)
        mixer.blend(Company)

    def test_retrieve(self):
        url = reverse('api_v1_app:company-detail', args=(self.company.pk,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.company.name)

    def test_list_by_district(self):
        url = reverse('api_v1_app:company-list', args=(self.district.pk,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_search_by_name(self):
        url_base = reverse('api_v1_app:company-list', args=(self.district.pk,))
        url = f'{url_base}?search={self.company.name}'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_search_by_product_name(self):
        price = mixer.blend(Price, company=self.company)
        url_base = reverse('api_v1_app:company-list', args=(self.district.pk,))
        url = f'{url_base}?search={price.product.name}'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_filter_by_product_price(self):
        price = mixer.blend(Price, price=100.50, company=self.company)
        url_base = reverse('api_v1_app:company-list', args=(self.district.pk,))

        url = f'{url_base}?price__gt={price.price-1}&price__lt={price.price+1}'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

        url = f'{url_base}?price__gt={price.price+1}&price__lt={price.price+1}'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

    def test_filter_by_product_category_name(self):
        price = mixer.blend(Price, price=100.50, company=self.company)
        url_base = reverse('api_v1_app:company-list', args=(self.district.pk,))

        url = f'{url_base}?product_category_name={price.product.category.name}'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

        url = f'{url_base}?product_category_name=Wrong category'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)
