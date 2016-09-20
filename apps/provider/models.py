from django.db import models
from apps.core.models import BaseModel


class Provider(BaseModel):
    name = models.CharField(max_length=20)