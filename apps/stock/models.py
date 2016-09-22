from django.db import models
from apps.product.models import Product
from apps.core.models import BaseModel
from apps.item_resource.models import ItemResource
from django.utils import timezone

from django.dispatch import receiver
from django.db.models.signals import post_save


class BaseStock(BaseModel):
    quantity = models.IntegerField(default=0)

    class Meta:
        abstract = True


class IOStockBase(BaseModel):
    date = models.DateTimeField(default=timezone.now)
    quantity = models.IntegerField(default=0)

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


@receiver(post_save, sender=Product)
def product_post_save(sender, *args, **kwargs):
    """
        When create product then create stock
    """
    if kwargs['created']:
        ProductStock(item=kwargs['instance']).save()


@receiver(post_save, sender=ItemResource)
def item_resource_post_save(sender, *args, **kwargs):
    """
        When create item resource then create stock
    """
    if kwargs['created']:
        ItemResourceStock(item=kwargs['instance']).save()


@receiver(post_save, sender=IOProductStock)
def io_product_stock_post_save(sender, *args, **kwargs):
    """
        When create Input product stock then __ on stock
    """
    if kwargs['created']:
        io = kwargs['instance']
        io.stock.quantity += io.quantity
        io.stock.save()

@receiver(post_save, sender=IOItemResourceStock)
def io_resource_stock_post_save(sender, *args, **kwargs):
    """
        When create Input resource stock then __ on stock
    """
    if kwargs['created']:
        io = kwargs['instance']
        io.stock.quantity += io.quantity
        io.stock.save()
