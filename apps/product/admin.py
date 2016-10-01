from django.contrib import admin

from .models import Product, ProductImage, ProductVariant, Category

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(ProductVariant)
