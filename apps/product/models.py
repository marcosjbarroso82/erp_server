from django.db import models
from apps.core.models import BaseModel


class Product(BaseModel):
    name = models.CharField(max_length=20)
    price = models.DecimalField(decimal_places=2, max_digits=12) # validators=[models.validators.MinValueValidator(0)])

