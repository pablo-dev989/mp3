from django.urls import path
from rest_framework import routers

from . import views
from .viewsets import ManufacturerViewSet, SmartphoneViewSet

router = routers.DefaultRouter()
router.register('manufacturer', ManufacturerViewSet)
router.register('smartphone', SmartphoneViewSet)


urlpatterns = [
    path('manufacturers/', views.manufacturers_index, name='manufacturers'),
    path('manufacturers/importar/', views.importar_marca, name='manufacturers_import'),
    path('smartphones/create/', views.smartphone_create, name='smartphone_create'),
]

urlpatterns += router.urls