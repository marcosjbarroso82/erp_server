from django.db import models
from apps.core.models import BaseModel
from django.utils import timezone
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class Balance(BaseModel):
    date = models.DateTimeField(default=timezone.now)
    amount = models.DecimalField(decimal_places=2, max_digits=12, default=0)
    description = models.TextField()
    type = models.IntegerField(choices=((0, 'output'), (1, 'input')))

    ticket_type = models.ForeignKey(ContentType, related_name='balances')
    ticket_id = models.PositiveIntegerField()
    ticket = GenericForeignKey('ticket_type', 'ticket_id')
