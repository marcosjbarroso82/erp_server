from django.db import models
from apps.core.models import BaseModel
from apps.order.models import OrderItem
from django.db.models import Sum


class Product(BaseModel):
    sku = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    price = models.DecimalField(decimal_places=2, max_digits=12) # validators=[models.validators.MinValueValidator(0)])
    description = models.TextField()


    @property
    def reserved_stock_quantity(self):
        # import ipdb; ipdb.set_trace()
        return self.stock.reserved_stock

    @property
    def available_stock_quantity(self):
        return self.available_stock_quantity

    @property
    def stock_quantity(self):
        return self.stock.quantity

    @property
    def available_stock_quantity(self):
        return self.stock_quantity - self.reserved_stock_quantity

    def get_price_per_item(self):
        return self.price

