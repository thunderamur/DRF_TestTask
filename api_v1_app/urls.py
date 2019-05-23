from django.urls import include, path
from rest_framework import routers

from api_v1_app import views

app_name = 'api_v1_app'

router = routers.DefaultRouter()
router.register(r'organization', views.CompanyDetailView, 'company')
router.register(r'product', views.ProductDetailView)
router.register(r'organizations/(?P<district_id>[0-9]+)', views.CompanyListView, 'company')


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
