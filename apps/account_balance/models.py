from django.db import models
from apps.core.models import BaseModel
from django.utils import timezone
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.utils import timezone


class Balance(BaseModel):
    pass

    @property
    def total(self):
        return 99


class Ticket(BaseModel):
    balance = models.ForeignKey(Balance)
    status = models.IntegerField(choices=((0, 'canceled'), (1, 'pending'), (2, 'closed')), default=1)
    type = models.IntegerField(choices=((0, 'output'), (1, 'input')))
    amount = models.DecimalField(decimal_places=2, max_digits=12, default=0)
    date = models.DateTimeField(default=timezone.now)

    actor_type = models.ForeignKey(ContentType, related_name='tickets')
    actor_id = models.PositiveIntegerField()
    actor = GenericForeignKey('actor_type', 'actor_id')
