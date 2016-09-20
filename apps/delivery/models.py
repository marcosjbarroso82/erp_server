from django.db import models
from apps.core.models import BaseModel
from apps.order.models import Order, OrderItem
from apps.address.models import Address
from apps.employee.models import Employee


DELIVERY_STATUS_OPTIONS = (
    (0, 'canceled'),
    (1, 'pending'),
    (3, 'completed')
)


class Distribution(BaseModel):
    date = models.DateTimeField()
    employee = models.ForeignKey(Employee)


class DeliveryGroup(BaseModel):
    order = models.OneToOneField(Order, related_name='delivery_group')
    status = models.IntegerField(choices=DELIVERY_STATUS_OPTIONS)
    address = models.ForeignKey(Address, on_delete=models.PROTECT)


class Delivery(BaseModel):
    group = models.ForeignKey(DeliveryGroup)
    status = models.IntegerField(choices=DELIVERY_STATUS_OPTIONS)
    item = models.ForeignKey(OrderItem)
    quantity = models.PositiveIntegerField()
    distribution = models.ForeignKey(Distribution)

