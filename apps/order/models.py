from django.db import models
from apps.core.models import BaseModel
from apps.client.models import Client
from apps.product.models import Product


ORDER_STATUS_OPTIONS = (
    (0, 'canceled'),
    (1, 'pending'),
    (3, 'completed'),
    (4, 'delivered'),
    (5, 'paid'),
)

class Order(BaseModel):
    client = models.ForeignKey(Client, related_name='orders')
    status = models.IntegerField(choices=ORDER_STATUS_OPTIONS)

    # Transaction Saved Fields
    total = models.DecimalField(decimal_places=2, max_digits=12, editable=False)


class OrderItem(BaseModel):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()

    # Transaction Saved Fields
    product_name = models.CharField(max_length=20, editable=False)
    price = models.DecimalField(decimal_places=2, max_digits=12, editable=False)