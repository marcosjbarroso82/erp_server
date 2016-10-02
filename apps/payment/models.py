from django.db import models
from django.utils.translation import ugettext_lazy as _
from apps.core.models import BaseModel
from apps.account_balance.models import Ticket
from django.utils import timezone
from django.db import transaction

PAYMENT_STATUS_CHOICES = (
    (0, 'Canceled'),
    (1, 'Pending'),
    (2, 'Payed')
)

PAYMENT_TYPE_CHOICES = (
    ('cash', _('cash')),
    ('check', _('cheque')),
    ('credit_card', _('credit card')),
    ('transder', _('transfer'))
)

class Payment(BaseModel):
    date = models.DateTimeField(default=timezone.now)
    type = models.CharField(choices=PAYMENT_TYPE_CHOICES, max_length=15)
    order = models.ForeignKey('order.Order', related_name='payments')
    amount = models.DecimalField(decimal_places=2, max_digits=12)
    ticket = models.OneToOneField(Ticket, null=True)
    status = models.IntegerField(default=1, choices=PAYMENT_STATUS_CHOICES)

    def __init__(self, *args, **kwargs):
        super(Payment, self).__init__(*args, **kwargs)
        self._status = self.status if self.status else 1
        # This need when using manager for created objetcs
        # Ex: Payment.objects.create()
        self.changed = True if self.pk else False

    def __str__(self):
        return "#%s , %s" %(self.id, self.get_status_display())

    def change_status(self):
        self.changed = True
        with transaction.atomic():
            if self.status == 2: # payed
                self._status = self.status
                self.save()
                self.order.check_payed() # Check order if all payed
            elif self.status == 0 and self._status == 2: # payed to cancel
                # TODO: ¿Que pasa aca? Aparte de cambiar la orden de estado
                self._status = self.status
                self.save()
                self.order.check_payed() # Check order if all payed
            else:
                self._status = self.status
                self.save()

    def save(self, *args, **kwargs):
        if self._status != self.status or not self.changed:
            self.change_status()
        else:
            super(Payment, self).save(*args, **kwargs)