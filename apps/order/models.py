from django.db import models
from apps.core.models import BaseModel
from apps.client.models import Client
from apps.account_balance.models import Ticket


ORDER_STATUS_OPTIONS = (
    (0, 'canceled'),
    (1, 'pending'),
    (2, 'completed'),
    (3, 'delivered'),
    (4, 'paid'),
)

class Order(BaseModel):
    client = models.ForeignKey(Client, related_name='orders')
    status = models.IntegerField(choices=ORDER_STATUS_OPTIONS)
    # Transaction Saved Fields
    total = models.DecimalField(decimal_places=2, max_digits=12, editable=False, default=0)
    ticket = models.OneToOneField(Ticket, null=True)

    def add_item(self, product, quantity, data={}, action='increment'):
        # TODO: borrar el item si fue modificado
        # try:

        reserved_stock = product.get_available_stock()

        if reserved_stock >= quantity:
            if self.items.filter(product=product).exists():
                item = self.items.filter(product=product).first()
                item.quantity += quantity
            else:
                item = OrderItem(order=self, product=product, quantity=quantity, price=product.get_price_per_item())
            item.save()




class OrderItem(BaseModel):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.PROTECT)
    product = models.ForeignKey('product.ProductVariant', on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()

    # Transaction Saved Fields
    product_name = models.CharField(max_length=20, editable=False)
    price = models.DecimalField(decimal_places=2, max_digits=12, editable=False)


    def save(self, *args, **kwargs):
        if not self.pk:
            self.product_name = self.product.name
            self.price = self.product.price

        return super(OrderItem, self).save(*args, **kwargs)