from datetime import datetime
from apps.product.models import Product as ProductVariant


class NewCartItem(object):
    def __init__(self, product, quantity, price, data, msg=''):
        self.product = product
        self.quantity = quantity
        self.price = price
        self.data = data
        self.msg = msg

    @property
    def sub_total(self):
        return self.quantity * self.price


class NewCart(object):
    def __init__(self, created_date=None,):
        self.created_date = created_date if created_date else datetime.now()

        self.updated_date = datetime.now()
        self.items = []

    @property
    def total(self):
        total = float(0)
        for item in self.items:
            total += float(item.sub_total)
        return total

    def add_item(self, product, quantity, data, action='increment'):
        # TODO: borrar el item si fue modificado
        try:
            variant = ProductVariant.objects.get(id=product)
        except:
            variant = None

        if variant:
            msg = ''
            # Checkear si otro item con la misma variacion ya reservo stock
            reserved_stock = 0
            for item in self.items:
                if item.product == product:
                    reserved_stock = reserved_stock + item.quantity

            stocked_quantity = variant.get_stock_quantity()
            available_quantity = stocked_quantity - reserved_stock

            if action == 'increment':
                for item in self.items:
                    if item.product == product:
                        if quantity > available_quantity:
                            item.quantity = item.quantity + available_quantity
                            item.msg = 'No hay suficiente stock para este item. Hemos ingresado para este item, el maximo disponible'
                        else:
                            item.quantity = item.quantity + quantity
                        break
                else: # this else belongs to the for loop and it's executed only if break instruction has no been executed.
                    if quantity > available_quantity:
                        new_quantity = available_quantity
                        msg = 'No hay suficiente stock para este item. Hemos ingresado para este item, el maximo disponible'
                    else:
                        new_quantity = quantity
                    if new_quantity > 0:
                        item = NewCartItem(product=product, quantity=new_quantity, price=variant.get_price_per_item(), data=data, msg=msg)
                        item.variant = variant
                        self.items.append(item)

            elif action == 'add':
                if quantity > available_quantity:
                    new_quantity = available_quantity
                    msg = 'No hay suficiente stock para este item. Hemos ingresado para este item, el maximo disponible'
                else:
                    new_quantity = quantity
                if new_quantity > 0:
                    item = NewCartItem(product=product, quantity=new_quantity, price=variant.get_price_per_item(), data=data, msg=msg)
                    item.variant = variant
                    self.items.append(item)
            elif action == 'replace':
                for item in self.items:
                    if item.product == product:
                        if quantity > available_quantity:
                            item.quantity = available_quantity
                            item.msg = 'No hay suficiente stock para este item. Hemos ingresado para este item, el maximo disponible'
                        else:
                            item.quantity = quantity
                        break
                else: # this else belongs to the for loop and it's executed only if break instruction has no been executed.
                    if quantity > available_quantity:
                        new_quantity = available_quantity
                        msg = 'No hay suficiente stock para este item. Hemos ingresado para este item, el maximo disponible'
                    else:
                        new_quantity = quantity
                    if new_quantity > 0:
                        item = NewCartItem(product=product, quantity=new_quantity, price=variant.get_price_per_item(), data=data, msg=msg)
                        item.variant = variant
                        self.items.append(item)