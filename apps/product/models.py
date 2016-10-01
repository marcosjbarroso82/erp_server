from django.db import models
from apps.core.models import BaseModel

import itertools
from django.template.defaultfilters import slugify


class Category(BaseModel):
    name = models.CharField(max_length=40)
    slug = models.SlugField(auto_created='name')

    def __init__(self, *args, **kwargs):
        super(Category, self).__init__(*args, **kwargs)
        self.old_name = self.name

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Generate slug
        if not self.pk or self.name != self.old_name:
            self.slug = orig = slugify(self.name)
            for x in itertools.count(1):
                qs = Category.objects.filter(slug=self.slug)
                qs = qs.exclude(pk=self.pk) if self.pk else qs
                if not qs.exists():
                    break
                self.slug = '%s-%d' % (orig, x)

        super(Category, self).save(*args, **kwargs)

class Product(BaseModel):
    name = models.CharField(max_length=40)
    category = models.ForeignKey(Category, related_name='products')
    price = models.DecimalField(decimal_places=2, max_digits=12)
    description = models.TextField()


class ProductVariant(BaseModel):
    product = models.ForeignKey(Product, related_name='variations')
    sku = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    price = models.DecimalField(decimal_places=2, max_digits=12) # validators=[models.validators.MinValueValidator(0)])

    @property
    def reserved_stock_quantity(self):
        return self.stock.reserved_stock

    @property
    def stock_quantity(self):
        return self.stock.quantity

    @property
    def available_stock_quantity(self):
        return self.stock.available_stock

    def get_price_per_item(self):
        return self.price


class ProductImage(BaseModel):
    image = models.ImageField(upload_to='product')
    product = models.ForeignKey(Product, related_name='images')