from django.db.models import fields
from rest_framework import serializers

from store.models import Category, Product


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name',)


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'title', 'category', 'price', 'image', 'description', 'in_stock',)
