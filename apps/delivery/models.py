from django.db import models
from apps.core.models import BaseModel
from apps.order.models import Order, OrderItem
from apps.address.models import Address
from apps.employee.models import Employee


DELIVERY_STATUS_OPTIONS = (
    (0, 'canceled'),
    (1, 'pending'),
    (2, 'completed')
)


class Distribution(BaseModel):
    date = models.DateTimeField()
    employee = models.ForeignKey(Employee)


class DeliveryGroup(BaseModel):
    order = models.ForeignKey(Order, related_name='delivery_groups')
    status = models.IntegerField(choices=DELIVERY_STATUS_OPTIONS, default=1)
    address = models.ForeignKey(Address, on_delete=models.PROTECT, null=True)
    distribution = models.ForeignKey(Distribution, null=True)


class Delivery(BaseModel):
    group = models.ForeignKey(DeliveryGroup)
    item = models.ForeignKey(OrderItem)
    quantity = models.PositiveIntegerField()


