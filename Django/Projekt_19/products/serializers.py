from rest_framework import serializers
from .models import Product

#   Dodane w ramach task 2 Lesson 25
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price']
