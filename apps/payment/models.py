from django.db import models
from django.utils.translation import ugettext_lazy as _
from apps.core.models import BaseModel
from apps.order.models import Order
from apps.account_balance.models import Ticket
from django.utils import timezone

PAYMENT_TYPE_CHOICES2 = (
    ('cash', _('cash')),
    ('check', _('cheque')),
    ('credit_card', _('credit card')),
    ('transder', _('transfer'))
)

PAYMENT_TYPE_CHOICES = (
    ('cash', _('cash')),
    ('check', _('cheque')),
    ('credit_card', _('credit card')),
    ('transder', _('transfer'))
)

class Payment(BaseModel):
    date = models.DateTimeField(default=timezone.now)
    type = models.CharField(choices=PAYMENT_TYPE_CHOICES, max_length=10)
    order = models.ForeignKey(Order)
    amount = models.DecimalField(decimal_places=2, max_digits=12)
    ticket = models.OneToOneField(Ticket, null=True)