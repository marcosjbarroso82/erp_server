from django.db import models
from apps.core.models import Person
from apps.address.models import Address


class Client(Person):
    address = models.OneToOneField(Address, null=True)



