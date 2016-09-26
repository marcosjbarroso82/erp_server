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
    def reserved_stock(self):
        return self.get_reserved_stock()


    def get_stock_quantity(self):
        return self.stock.quantity

    def get_reserved_stock(self):
        reserved = OrderItem.objects.filter(product=self, order__status=1).aggregate(Sum('quantity'))
        return reserved.get('quantity__sum', 0)

    def get_available_stock(self):
        return self.get_stock_quantity() - self.get_reserved_stock()

    def get_price_per_item(self):
        return 7

