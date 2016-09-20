from django.db import models
from apps.product.models import Product
from apps.core.models import BaseModel


class BaseStock(BaseModel):
    quantity = models.IntegerField()

    class Meta:
        abstract = True


class ProductStock(BaseStock):
    item = models.OneToOneField(Product)