from django.db import models
from apps.core.models import BaseModel


class Address(BaseModel):
    street = models.CharField(max_length=50)
