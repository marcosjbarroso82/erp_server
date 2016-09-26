from django.db import models
from apps.core.models import BaseModel
from apps.client.models import Client
from apps.product.models import Product
from apps.account_balance.models import Ticket


ORDER_STATUS_OPTIONS = (
    (0, 'canceled'),
    (1, 'pending'),
    (2, 'completed'),
    (3, 'delivered'),
    (4, 'paid'),
)

class Order(BaseModel):
    client = models.ForeignKey(Client, related_name='orders')
    status = models.IntegerField(choices=ORDER_STATUS_OPTIONS)
    # Transaction Saved Fields
    total = models.DecimalField(decimal_places=2, max_digits=12, editable=False, default=0)
    ticket = models.OneToOneField(Ticket, null=True)

    def add_item(self, product, quantity, data={}, action='increment'):
        # TODO: borrar el item si fue modificado
        # try:

        if product:
            # msg = ''
            # Checkear si otro item con la misma variacion ya reservo stock
            reserved_stock = 0
            for item in self.items.all():
                if item.product == product:
                    reserved_stock = reserved_stock + item.quantity

            stocked_quantity = product.get_stock_quantity()
            available_quantity = stocked_quantity - reserved_stock

            if action == 'increment':
                for item in self.items.all():
                    if item.product == product:
                        if quantity > available_quantity:
                            item.quantity = item.quantity + available_quantity
                            # item.msg = 'No hay suficiente stock para este item. Hemos ingresado para este item, el maximo disponible'
                        else:
                            item.quantity = item.quantity + quantity
                        break
                else: # this else belongs to the for loop and it's executed only if break instruction has no been executed.
                    if quantity > available_quantity:
                        new_quantity = available_quantity
                        # msg = 'No hay suficiente stock para este item. Hemos ingresado para este item, el maximo disponible'
                    else:
                        new_quantity = quantity
                    if new_quantity > 0:
                        item = OrderItem(order=self, product=product, quantity=new_quantity, price=product.get_price_per_item())
                        item.product = product
                        # self.items.append(item)

            elif action == 'add':
                if quantity > available_quantity:
                    new_quantity = available_quantity
                    # msg = 'No hay suficiente stock para este item. Hemos ingresado para este item, el maximo disponible'
                else:
                    new_quantity = quantity
                if new_quantity > 0:
                    item = OrderItem(order=self, product=product, quantity=new_quantity, price=product.get_price_per_item())
                    item.product = product
                    # self.items.append(item)
            elif action == 'replace':
                for item in self.items.all():
                    if item.product == product:
                        if quantity > available_quantity:
                            item.quantity = available_quantity
                            # item.msg = 'No hay suficiente stock para este item. Hemos ingresado para este item, el maximo disponible'
                        else:
                            item.quantity = quantity
                        break
                else: # this else belongs to the for loop and it's executed only if break instruction has no been executed.
                    if quantity > available_quantity:
                        new_quantity = available_quantity
                        # msg = 'No hay suficiente stock para este item. Hemos ingresado para este item, el maximo disponible'
                    else:
                        new_quantity = quantity
                    if new_quantity > 0:
                        item = OrderItem(order=self, product=product, quantity=new_quantity, price=product.get_price_per_item())
                        item.product = product
                        # self.items.append(item)
            # import ipdb; ipdb.set_trace()
            item.save()



class OrderItem(BaseModel):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()

    # Transaction Saved Fields
    product_name = models.CharField(max_length=20, editable=False)
    price = models.DecimalField(decimal_places=2, max_digits=12, editable=False)


    def save(self, *args, **kwargs):
        if not self.pk:
            self.product_name = self.product.name
            self.price = self.product.price

        return super(OrderItem, self).save(*args, **kwargs)