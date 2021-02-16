from rest_framework import viewsets
from . import models
from . import serializers

class client_viewset(viewsets.ModelViewSet):
    queryset = models.Clients.objects.all()
    serializer_class = serializers.client_serializer

class bill_viewset(viewsets.ModelViewSet):
    queryset = models.Bills.objects.all()
    serializer_class = serializers.bill_serializer

class product_viewset(viewsets.ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.product_serializer

