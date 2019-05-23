import django_filters

from rest_framework import viewsets, mixins, generics, filters
from django_filters.rest_framework import DjangoFilterBackend

from api_v1_app import serializers
from mainapp.models import Company, Product


class CompanyDetailView(mixins.RetrieveModelMixin,
                        viewsets.GenericViewSet):
    queryset = Company.objects.all()
    serializer_class = serializers.CompanySerializer


class ProductDetailView(mixins.RetrieveModelMixin,
                        viewsets.GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer


class CompanyFilter(django_filters.FilterSet):
    price__gt = django_filters.NumberFilter(
        field_name='price__price', lookup_expr='gt', label='Цена товара/услуги больше чем')
    price__lt = django_filters.NumberFilter(
        field_name='price__price', lookup_expr='lt', label='Цена товара/услуги меньше чем')

    product_category_name = django_filters.CharFilter(
        field_name='price__product__category__name', lookup_expr='icontains',
        label='Название категории товара/услуги содержит')


class CompanyListView(mixins.ListModelMixin,
                      viewsets.GenericViewSet):
    serializer_class = serializers.CompanySerializer
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)
    search_fields = ('name', 'price__product__name')
    filterset_class = CompanyFilter

    def get_queryset(self):
        district_id = self.kwargs.get('district_id')
        queryset = Company.objects
        if district_id:
            queryset = queryset.filter(districts__id=district_id).distinct().order_by('name')
        else:
            queryset = None
        return queryset
