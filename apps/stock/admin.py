from django.contrib import admin

from .models import IOItemResourceStock, IOProductStock, ProductStock, ItemResourceStock

admin.site.register(IOItemResourceStock)
admin.site.register(ItemResourceStock)

admin.site.register(IOProductStock)
admin.site.register(ProductStock)
