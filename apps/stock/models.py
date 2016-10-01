from django.db import models
from apps.product.models import ProductVariant
from apps.core.models import BaseModel
from apps.item_resource.models import ItemResource
from django.utils import timezone

from django.dispatch import receiver
from django.db.models.signals import post_save
from apps.order.models import OrderItem
from apps.delivery.models import Delivery
from django.db.models import Sum


class BaseStock(BaseModel):
    quantity = models.IntegerField(default=0)

    class Meta:
        abstract = True


class IOStockBase(BaseModel):
    date = models.DateTimeField(default=timezone.now)
    quantity = models.IntegerField(default=0)
    note = models.TextField(null=True, blank=True)

    class Meta:
        abstract = True


class ProductStock(BaseStock):
    item = models.OneToOneField(ProductVariant, related_name='stock')

    @property
    def reserved_stock(self):
        #import pdb; pdb.set_trace()
        stock = OrderItem.objects.filter(product=self.item, order__status=1).aggregate(Sum('quantity')).get('quantity__sum', 0)
        quantity = stock if stock else 0
        stock_delivered_to_order_pending = Delivery.objects.filter(item__product=self.item, group__status=2).aggregate(Sum('quantity')).get('quantity__sum', 0)
        quantity -= stock_delivered_to_order_pending if stock_delivered_to_order_pending else 0
        return quantity

    @property
    def available_stock(self):
        return self.quantity - self.reserved_stock

    def consume_stock(self, quantity, note):
        IOProductStock.objects.create(stock=self, quantity=-quantity, note=note)

    def add_stock(self, quantity, note):
        IOProductStock.objects.create(stock=self, quantity=quantity, note=note)


class IOProductStock(IOStockBase):
    stock = models.ForeignKey(ProductStock, related_name='details')


class ItemResourceStock(BaseStock):
    item = models.OneToOneField(ItemResource, related_name='stock')

class IOItemResourceStock(IOStockBase):
    stock = models.ForeignKey(ItemResourceStock, related_name='details')


@receiver(post_save, sender=ProductVariant)
def product_post_save(sender, *args, **kwargs):
    """
        When create product variant then create stock
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
