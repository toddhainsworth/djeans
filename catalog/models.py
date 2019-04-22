from django.db import models
from enum import Enum

class StatusChoice(Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"

class PriceType(Enum):
    REGULAR = "regular"
    SPECIAL = "special"
    GROUP = "group"


class Category(models.Model):
    title = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=[(status.value, status.name.capitalize()) for status in StatusChoice])
    url_key = models.CharField(max_length=50) # We'll generate one if not provided
    description = models.TextField()

    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=[(status.value, status.name.capitalize()) for status in StatusChoice])
    url_key = models.CharField(max_length=50) # We'll generate one if not provided
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=1000, default=0.0)
    special_price = models.DecimalField(decimal_places=2, max_digits=1000, default=0.0)

    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.title
