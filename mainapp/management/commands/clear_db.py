from django.core.management.base import BaseCommand

from mainapp.models import Price, District, Company, CompanyGroup, Product, Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        objects = [
            Price,
            Product,
            Category,
            Company,
            District,
            CompanyGroup,
        ]
        for obj in objects:
            print(obj.objects.all().delete())
