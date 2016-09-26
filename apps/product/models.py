from django.db import models
from apps.core.models import BaseModel


class Product(BaseModel):
    sku = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    price = models.DecimalField(decimal_places=2, max_digits=12) # validators=[models.validators.MinValueValidator(0)])
    description = models.TextField()

    def get_stock_quantity(self):
        return self.stock.quantity

    def get_price_per_item(self):
        return 7

