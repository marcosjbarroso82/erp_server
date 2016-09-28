from django.db import models
from apps.core.models import BaseModel
from apps.order.models import OrderItem
from django.db.models import Sum


class Category(BaseModel):
    name = models.CharField(max_length=40)
    slug = models.SlugField(auto_created='name')


class Product(BaseModel):
    name = models.CharField(max_length=40)
    category = models.ForeignKey(Category, related_name='products')


class ProductVariant(BaseModel):
    product = models.ForeignKey(Product, related_name='variations')
    sku = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    price = models.DecimalField(decimal_places=2, max_digits=12) # validators=[models.validators.MinValueValidator(0)])
    description = models.TextField()

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