from django.db import models
from apps.core.models import BaseModel


class Delivery(BaseModel):
    date = models.DateTimeField()
