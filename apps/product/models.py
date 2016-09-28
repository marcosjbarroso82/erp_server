from django.db import models
from apps.core.models import BaseModel
from apps.order.models import OrderItem
from django.db.models import Sum
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
    def reserved_stock(self):
        return self.get_reserved_stock()

    @property
    def available_stock(self):
        return self.get_available_stock()

    @property
    def stock_quantity(self):
        return self.get_stock_quantity()

    def get_stock_quantity(self):
        return self.stock.quantity

    def get_reserved_stock(self):
        stock = OrderItem.objects.filter(product=self, order__status=1).aggregate(Sum('quantity')).get('quantity__sum', 0)
        return stock if stock else 0

    def get_available_stock(self):
        return self.get_stock_quantity() - self.get_reserved_stock()

    def get_price_per_item(self):
        return 7


class ProductImage(BaseModel):
    image = models.ImageField(upload_to='product')
    product = models.ForeignKey(Product, related_name='images')