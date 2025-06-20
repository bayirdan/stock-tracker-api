from django.db import models

class Category(models.Model):
  name = models.CharField(max_length=100, unique=True)

  class Meta:
    verbose_name_plural = 'Categories'

  def __str__(self):
    return self.name
  
class Product(models.Model):
  name = models.CharField(max_length=200, unique=True)
  description = models.TextField(blank=True, null=True)
  category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
  price = models.DecimalField(max_digits=10, decimal_places=2)
  stock_quantity = models.IntegerField(default=0)
  sku = models.CharField(max_length=50, unique=True, blank=True, null=True)
  created_at = models.DateField(auto_now=True)
  updated_at = models.DateField(auto_now=True)

  class Meta:
    ordering = ['name']

  def __str__(self):
      return self.name

