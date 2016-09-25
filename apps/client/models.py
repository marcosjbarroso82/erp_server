from django.db import models
from apps.core.models import Person
from apps.address.models import Address
from apps.account_balance.models import Balance

class Client(Person):
    address = models.OneToOneField(Address, null=True)
    balance = models.OneToOneField(Balance)




