from rest_framework import serializers
from .models import Product, Category

class CategorySerializers(serializers.ModelSerializer):
  class Meta:
    model = Category
    fields = '__all__'

class ProductSerializers(serializers.ModelSerializer):
  category_name = serializers.ReadOnlyField(source='category.name')

  class Meta:
    model = Product
    fields = '__all__'
    read_only_fields = ('created_at', 'updated_at')