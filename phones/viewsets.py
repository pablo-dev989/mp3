from rest_framework import viewsets

from phones.models import Manufacturer, Smartphone
from phones.serializer import ManufacturerSerializer, SmartphoneSerializer


class ManufacturerViewSet(viewsets.ModelViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer

class SmartphoneViewSet(viewsets.ModelViewSet):
    queryset = Smartphone.objects.all()
    serializer_class = SmartphoneSerializer