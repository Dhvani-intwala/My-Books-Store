from django.db import models
from products.models import Category


class Book_discount(models.Model):
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254,  default='')
    sku = models.CharField(max_length=254, null=True, blank=True)
    books_type = models.CharField(max_length=254,  default='')
    auth_name = models.CharField(max_length=254, default='')
    description = models.TextField(default='')
    year = models.PositiveIntegerField(null=False, blank=False, default='')
    price = models.DecimalField(max_digits=6, decimal_places=2, null=False,
                                blank=False)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True,
                                 blank=True)
    image = models.ImageField(null=True, blank=True)
    stock = models.PositiveIntegerField(null=False, blank=False, default=100)
    discount = models.DecimalField(max_digits=3, decimal_places=2, default=0.50)

    def discounted_price(self):
        return self.price * (1 - self.discount)
