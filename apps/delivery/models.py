from django.db import models
from apps.core.models import BaseModel
from apps.order.models import Order
from apps.address.models import Address
from apps.employee.models import Employee


class Distribution():
    date = models.DateTimeField()
    employee = models.ForeignKey(Employee)



DELIVERY_STATUS_OPTIONS = (
    (0, 'canceled'),
    (1, 'pending'),
    (3, 'completed')
)

class Delivery(BaseModel):
    order = models.ForeignKey(Order, related_name='deliveries')
    status = models.IntegerField(choices=DELIVERY_STATUS_OPTIONS)
    address = models.ForeignKey(Address, on_delete=models.PROTECT)
    distribution = models.ForeignKey(Distribution)

