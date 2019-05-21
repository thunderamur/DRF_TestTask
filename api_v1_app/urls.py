from django.urls import include, path

from rest_framework import routers

from api_v1_app import views

router = routers.DefaultRouter()
router.register(r'product', views.ProductViewSet)

# router.register(r'records/(?P<date>[0-9]{4}-[0-9]{2}-[0-9]{2})', RecordViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('organizations/<int:district_id>/', views.company, name='company_list'),
    path('organization/<int:id>/', views.company_detail, name='company_detail'),
]
