from django.core.exceptions import ObjectDoesNotExist

from rest_framework import viewsets, mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api_v1_app import serializers
from mainapp.models import Company, Product


class ProductViewSet(mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet):
    queryset = Product.objects.order_by('name')
    serializer_class = serializers.ProductSerializer


@api_view(['GET'])
def company(req, district_id):
    if req.method == 'GET':
        company_list = Company.objects.filter(districts__id=district_id).order_by('name')
        serializer = serializers.CompanySerializer(company_list, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def company_detail(req, id):
    try:
        company = Company.objects.get(pk=id)
    except ObjectDoesNotExist:
        return Response(status=404)

    if req.method == 'GET':
        serializer = serializers.CompanySerializer(company)
        return Response(serializer.data)
