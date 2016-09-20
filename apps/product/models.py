from django.db import models
from apps.core.models import BaseModel


class Product(BaseModel):
    name = models.CharField(max_length=20)
    price = models.DecimalField() # validators=[models.validators.MinValueValidator(0)])



