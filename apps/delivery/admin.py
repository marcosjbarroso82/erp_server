from django.contrib import admin

from .models import Delivery, DeliveryGroup, Distribution

admin.site.register(DeliveryGroup)
admin.site.register(Delivery)
admin.site.register(Distribution)
# Register your models here.
