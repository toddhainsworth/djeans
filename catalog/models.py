from django.db import models
from enum import Enum

class StatusChoice(Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"

class PriceType(Enum):
    REGULAR = "regular"
    SPECIAL = "special"
    GROUP = "group"

class Product(models.Model):
    title = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=[(status, status.value) for status in StatusChoice])
    url_key = models.CharField(max_length=50) # We'll generate one if not provided
    description = models.TextField()

    def __str__(self):
        self.title

class ProductPrice(models.Model):
    amount = models.DecimalField(decimal_places=2, max_digits=1000)
    price_type = models.CharField(max_length=20, choices=[(price_type, price_type.value) for price_type in PriceType])
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        "${}".format(self.amount)

class Category(models.Model):
    title = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=[(status, status.value) for status in StatusChoice])
    url_key = models.CharField(max_length=50) # We'll generate one if not provided
    description = models.TextField()

    products = models.ManyToManyField(Product)

    def __str__(self):
        self.title
