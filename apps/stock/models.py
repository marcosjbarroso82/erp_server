from django.db import models
from apps.product.models import Product
from apps.core.models import BaseModel
from apps.item_resource.models import ItemResource
from django.utils import timezone


class BaseStock(BaseModel):
    quantity = models.IntegerField()

    class Meta:
        abstract = True


class IOStockBase(BaseModel):
    date = models.DateTimeField(default=timezone.now)
    quantity = models.IntegerField()

    class Meta:
        abstract = True


class ProductStock(BaseStock):
    item = models.OneToOneField(Product)

class IOProductStock(IOStockBase):
    stock = models.ForeignKey(ProductStock)


class ItemResourceStock(BaseStock):
    item = models.OneToOneField(ItemResource)

class IOItemResourceStock(IOStockBase):
    stock = models.ForeignKey(ItemResourceStock)