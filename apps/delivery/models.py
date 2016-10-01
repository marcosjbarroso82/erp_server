from django.db import models
from apps.core.models import BaseModel

from django.db import transaction

DELIVERY_STATUS_OPTIONS = (
    (0, 'canceled'),
    (1, 'pending'),
    (2, 'delivered')
)


class Distribution(BaseModel):
    date = models.DateTimeField()
    employee = models.ForeignKey('employee.Employee', related_name='Distributions')


class DeliveryGroup(BaseModel):
    order = models.ForeignKey('order.Order', related_name='delivery_groups')
    status = models.IntegerField(choices=DELIVERY_STATUS_OPTIONS, default=1)
    address = models.ForeignKey('address.Address', on_delete=models.PROTECT, null=True)
    distribution = models.ForeignKey('Distribution', null=True)

    def __init__(self, *args, **kwargs):
        super(DeliveryGroup, self).__init__(*args, **kwargs)
        self._status = self.status if self.status else 1

    def __str__(self):
        return "#%s , %s" %(self.id, self.get_status_display())

    def change_status(self):
        with transaction.atomic():
            if self.status == 2 and self._status == 1: # pending to delivered
                self._status = 2
                self.save()
                for delivery in self.deliveries.all():
                    delivery.consume_stock() # Consumed stock
                self.order.check_delivered() # Check order if all delivered
            elif self.status == 0 and self._status == 2: # delivered to cancel
                # TODO: ¿Volver a meter el stock?
                pass
            else:
                self._status = self.status
                self.save()

    def save(self, *args, **kwargs):
        if self._status != self.status:
            self.change_status()
        else:
            super(DeliveryGroup, self).save(*args, **kwargs)


class Delivery(BaseModel):
    group = models.ForeignKey(DeliveryGroup, related_name='deliveries')
    item = models.ForeignKey('order.OrderItem', related_name='deliveries')
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return "%s : (delivery: %s)" % (self.item, self.quantity)

    def consume_stock(self):
        self.item.product.stock.consume_stock(quantity=self.quantity, note='order: ' + str(self.group.order.pk))

