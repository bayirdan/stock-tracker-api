from django.shortcuts import render
from rest_framework import viewsets
from .models import Product, Category
from .serializers import CategorySerializers, ProductSerializers

class CategoryViewSet(viewsets.ModelViewSet):
  queryset = Category.objects.all()
  serializer_class = CategorySerializers

class ProductViewSet(viewsets.ModelViewSet):
  queryset = Product.objects.all()
  serializer_class = ProductSerializers
