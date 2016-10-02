from django.test import TestCase
from .models import Order, OrderItem
from apps.client.models import Client
from apps.product.models import ProductVariant
from decimal import Decimal
from apps.delivery.models import DeliveryGroup, Delivery


class OrderTestCase(TestCase):
    fixtures = ['db.json', ]

    def get_client(self):
        return Client.objects.get(pk=1)

    def test_order_item_effect_on_available_stock(self):
        """Check if order items affect to available stock when create order pending"""
        q1 = 5 # Quantity 1
        q2 = 2 # Quantity 2
        p = ProductVariant.objects.get(pk=1) # Product
        initial_available_stock = p.available_stock_quantity
        order = Order.objects.create(client=self.get_client(), status=1)

        order.add_item(p, q1)
        self.assertEqual(ProductVariant.objects.get(pk=p.pk).available_stock_quantity, initial_available_stock - q1)

        order.add_item(p, q2)
        self.assertEqual(ProductVariant.objects.get(pk=p.pk).available_stock_quantity, initial_available_stock - q1 - q2)

    def test_create_item_not_available_stock(self):
        """Check create order item with product not available stock"""
        product = ProductVariant.objects.get(pk=1)
        order = Order.objects.create(client=self.get_client(), status=1)
        order.add_item(product, product.available_stock_quantity + 1)
        self.assertEqual(len(order.items.all()), 0)

    def test_total_order(self):
        """
         Check total on order
        """
        q1 = 5 # Quantity 1
        q2 = 2 # Quantity 2
        q3 = 1 # Quantity 3
        p1 = ProductVariant.objects.get(pk=1) # Product 1
        p2 = ProductVariant.objects.get(pk=2) # Product 2

        order = Order.objects.create(client=self.get_client(), status=1)

        order.add_item(p1, q1)
        self.assertEqual(Order.objects.get(pk=order.pk).total, Decimal(p1.price*q1))

        order.add_item(p1, q2)
        self.assertEqual(Order.objects.get(pk=order.pk).total, Decimal(p1.price * (q1+q2)))

        order.add_item(p2, q3)
        self.assertEqual(Order.objects.get(pk=order.pk).total, Decimal  ((p1.price * (q1+q2))) + (p2.price * q3))

    def test_order_delivered_with_one_delivery_group(self):
        q = 2 # Quantity
        p = ProductVariant.objects.get(pk=1) # Product
        order = Order.objects.create(client=self.get_client(), status=1)
        order.add_item(p, q)
        for dg in order.delivery_groups.all():
            dg.status = 2
            dg.save()

        self.assertIs(order.delivered, True)

    def test_order_delivered_with_some_delivery_group(self):
        q = 2 # Quantity
        p = ProductVariant.objects.get(pk=1) # Product
        order = Order.objects.create(client=self.get_client(), status=1)
        oi = order.add_item(p, q) # OrderItem

        dg1 = order.delivery_groups.first() # DeliveryGroup 1
        d = dg1.deliveries.get(item__product=p.pk) # Get delivery for change quantity
        d.quantity = 1
        d.save()

        # Change status to delivered for DeliveryGroup 1
        dg1.status = 2
        dg1.save()

        # Check if order is delivered
        self.assertIs(order.delivered, False)

        dg2 = DeliveryGroup.objects.create(address=self.get_client().address, status=1, order=order) # DeliveryGroup 2
        Delivery.objects.create(group=dg2, item=oi, quantity=1)

        # Change status to delivered for DeliveryGroup 2
        dg2.status = 2
        dg2.save()

        self.assertIs(order.delivered, True)

    def test_order_payed(self):
        pass