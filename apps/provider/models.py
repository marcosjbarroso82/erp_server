from django.db import models
from apps.core.models import BaseModel
from apps.account_balance.models import Balance


class Provider(BaseModel):
    name = models.CharField(max_length=20)
    balance = models.OneToOneField(Balance)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.pk:
            balance = Balance()
            balance.save()
            self.balance = balance
        super().save(force_insert, force_update, using, update_fields)