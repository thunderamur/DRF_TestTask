from rest_framework.serializers import ModelSerializer

from mainapp.models import Company, Product


class CompanySerializer(ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
