from django.db import models
from apps.core.models import BaseModel
from apps.client.models import Client
from apps.account_balance.models import Ticket
from apps.delivery.models import Delivery
from django.db.models import Sum
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.db import transaction

ORDER_STATUS_OPTIONS = (
    (0, 'canceled'),
    (1, 'pending'),
    (2, 'completed'),
    (3, 'issued'),
)


class Order(BaseModel):
    client = models.ForeignKey(Client, related_name='orders')
    status = models.IntegerField(choices=ORDER_STATUS_OPTIONS)
    # Transaction Saved Fields
    total = models.DecimalField(decimal_places=2, max_digits=12, editable=False, default=0)
    ticket = models.OneToOneField(Ticket, null=True)

    delivered = models.BooleanField(default=False)
    payed = models.BooleanField(default=False)

    def __init__(self, *args, **kwargs):
        super(Order, self).__init__(*args, **kwargs)
        self._status = self.status if self.status else 1

    def change_status(self):
        with transaction.atomic():
            if self.status == 0: # Canceled order
                self._status = self.status
                self.save()
                for d_group in self.delivery_groups.all():
                    d_group.status = 0
                    d_group.save()
                for payment in self.payments.all():
                    payment.status = 0
                    payment.save()
            else:
                self._status = self.status
                self.save()

    def check_delivered(self):
        for item in self.items.all():
            quantity = Delivery.objects.filter(item=item, group__status=2, group__order=self)\
                .aggregate(Sum('quantity')).get('quantity__sum', 0)
            quantity_item_delivered = quantity if quantity else 0
            if item.quantity > quantity_item_delivered:
                self.delivered = False
                self.save()
                return False

        self.delivered = True
        self.save()

    def check_payed(self):
        total_payments_amount = self.payments.filter(status=2).aggregate(Sum('amount')).get('amount__sum', 0)
        self.payed = True if total_payments_amount and self.total <= total_payments_amount else False
        self.save()

    def __str__(self):
        return "#%s , $%s (%s)" %(self.id, self.total, self.get_status_display())


    def add_item(self, product, quantity, action='increment', *args, **kwargs):
        if product.available_stock_quantity >= quantity:
            if self.items.filter(product=product).exists():
                item = self.items.filter(product=product).first()
                item.quantity += quantity
            else:
                item = OrderItem(order=self, product=product, quantity=quantity, price=product.get_price_per_item())
            item.save()

    def save(self, *args, **kwargs):
        if self._status != self.status:
            self.change_status()
        else:
            super(Order, self).save(*args, **kwargs)


class OrderItem(BaseModel):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.PROTECT)
    product = models.ForeignKey('product.ProductVariant', on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()

    # Transaction Saved Fields
    product_name = models.CharField(max_length=20, editable=False)
    price = models.DecimalField(decimal_places=2, max_digits=12, editable=False)

    def __str__(self):
        return "(Order#%s) %s : %s" % (self.order.pk, self.product_name, self.quantity)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.product_name = self.product.name
            self.price = self.product.price

        return super(OrderItem, self).save(*args, **kwargs)


@receiver(post_save, sender=OrderItem)
def order_item_post_save(sender, *args, **kwargs):
    """
        When create product variant then create stock
    """
    total_amount = 0
    order = kwargs['instance'].order
    for item in order.items.all():
        total_amount += item.quantity * item.price

    order.total = total_amount
    order.save()