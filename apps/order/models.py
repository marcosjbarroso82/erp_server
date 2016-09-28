from django.db import models
from apps.core.models import BaseModel
from apps.client.models import Client
from apps.account_balance.models import Ticket


ORDER_STATUS_OPTIONS = (
    (0, 'completed'),
    (1, 'pending'),
    (2, 'canceled'),
    (3, 'issued'),
)

ORDER_PAYMENT_STATUS_OPTIONS = (
    (0, 'completed'),
    (1, 'pending'),
    (2, 'canceled'),
    (3, 'issued'),
)

ORDER_DELIVERY_STATUS_OPTIONS = (
    (0, 'completed'),
    (1, 'pending'),
    (2, 'canceled'),
    (3, 'issued'),
)

class Order(BaseModel):
    client = models.ForeignKey(Client, related_name='orders')
    _status = models.IntegerField(choices=ORDER_STATUS_OPTIONS, editable=False)
    delivery_status = models.IntegerField(choices=ORDER_DELIVERY_STATUS_OPTIONS, default=1)
    payment_status = models.IntegerField(choices=ORDER_PAYMENT_STATUS_OPTIONS, default=1)
    # Transaction Saved Fields
    total = models.DecimalField(decimal_places=2, max_digits=12, editable=False, default=0)
    ticket = models.OneToOneField(Ticket, null=True)

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        # import ipdb; ipdb.set_trace()
        # Cancell Pending Order
        if self._status == 1 and value == 2:
            if self.is_delivered or self.is_paid:
                # Issued Order
                self._status = 3
            else:
                # Cancel Order
                self._status = 0
        # Complete Pending Order
        elif self._status == 1 and value == 0:
            self.is_delivered = True
            self.is_paid = True
            self._status = value
        else:
            self._status = value
        if self.pk:
            self.save()

    @property
    def is_delivered(self):
        return True if self.delivery_status == 0 else False

    @is_delivered.setter
    def is_delivered(self, value):
        self.delivery_status = value
        for order_item in OrderItem.objects.filter(order=self):
            order_item.consume_stock()
        self.save()

    @property
    def is_paid(self):
        return True if self.payment_status == 0 else False

    @is_paid.setter
    def is_paid(self, value):
        # Change only if new status if Paid
        if value:
            self.payment_status = 0
        self.save()

    def add_item(self, product, quantity, data={}, action='increment'):
        reserved_stock = product.available_stock_quantity

        if reserved_stock >= quantity:
            if self.items.filter(product=product).exists():
                item = self.items.filter(product=product).first()
                item.quantity += quantity
            else:
                item = OrderItem(order=self, product=product, quantity=quantity, price=product.get_price_per_item())
            item.save()

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):

        super().save(force_insert, force_update, using, update_fields)


class OrderItem(BaseModel):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.PROTECT)
    product = models.ForeignKey('product.Product', on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()

    # Transaction Saved Fields
    product_name = models.CharField(max_length=20, editable=False)
    price = models.DecimalField(decimal_places=2, max_digits=12, editable=False)

    def consume_stock(self):
        self.product.stock.consume_stock(quantity=self.quantity, note='order: ' + str(self.order.pk))

    def save(self, *args, **kwargs):
        if not self.pk:
            self.product_name = self.product.name
            self.price = self.product.price

        return super(OrderItem, self).save(*args, **kwargs)