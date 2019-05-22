from django.core.management.base import BaseCommand
from mixer.backend.django import mixer
import random

from mainapp.models import Price, District, Company, CompanyGroup, Product, Category


COMPANY_GROUPS_NUM = 2
DISTRICTS_NUM = 5
COMPANY_NUM = 5
CATEGORY_NUM = 5
PRODUCT_NUM = 10
PRICE_NUM = 20


class Command(BaseCommand):
    def handle(self, *args, **options):
        print('CompanyGroup')
        company_groups = mixer.cycle(COMPANY_GROUPS_NUM).blend(CompanyGroup)

        print('District')
        districts = mixer.cycle(DISTRICTS_NUM).blend(District)

        print('Company')
        companies = mixer.cycle(COMPANY_NUM).blend(
            Company,
            company_group=lambda: random.choice(company_groups),
            districts=lambda: random.sample(districts, random.randint(1, DISTRICTS_NUM)),
        )

        print('Category')
        categories = mixer.cycle(CATEGORY_NUM).blend(Category)

        print('Product')
        products = mixer.cycle(PRODUCT_NUM).blend(
            Product,
            category=lambda: random.choice(categories),
        )

        print('Price')
        mixer.cycle(PRICE_NUM).blend(
            Price,
            price=lambda: random.random() * 1e5,
            product=lambda: random.choice(products),
            company=lambda: random.choice(companies),
        )
