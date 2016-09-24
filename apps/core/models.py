from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True


class Person(BaseModel):
    first_name = models.CharField(max_length=20)

    class Meta:
        abstract = True

