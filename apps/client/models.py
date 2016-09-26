from django.db import models
from apps.core.models import Person
from apps.address.models import Address
from apps.account_balance.models import Balance

class Client(Person):
    address = models.OneToOneField(Address, null=True)
    balance = models.OneToOneField(Balance)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.pk:
            balance = Balance()
            balance.save()
            self.balance = balance
        super().save(force_insert, force_update, using, update_fields)




