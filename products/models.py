
from django.db import models


class Category(models.Model):
    """Category model"""
    class Meta:
        """Override Meta class"""
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    """Product model"""
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    sku = models.CharField(max_length=254, null=True, blank=True)
    books_type = models.CharField(max_length=254)
    auth_name = models.CharField(max_length=254)
    description = models.TextField()
    year = models.PositiveIntegerField(null=False, blank=False)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=False,
                                blank=False)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True,
                                 blank=True)
    image = models.ImageField(null=True, blank=True)
    stock = models.PositiveIntegerField(null=False, blank=False)

    def __str__(self):
        return self.name
