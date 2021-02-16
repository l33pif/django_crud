from rest_framework import serializers
from .models import Clients, Bills, Product

class client_serializer(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields = '__all__'

class bill_serializer(serializers.ModelSerializer):
    class Meta:
        model = Bills
        fields = '__all__'

class product_serializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
