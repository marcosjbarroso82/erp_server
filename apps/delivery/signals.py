from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.order.models import Order, OrderItem
from apps.delivery.models import DeliveryGroup, Delivery


@receiver(post_save, sender=Order)
def create_delivery_group(sender, **kwargs):
    print("create_delivery_group")
    if kwargs.get('created'):
        # import ipdb; ipdb.set_trace()
        delivery_group = DeliveryGroup.objects.create(order=kwargs['instance'])
        print("create_delivery_group " + str(delivery_group.pk))
    else:
        import ipdb; ipdb.set_trace()
    print(20*"*")
    print(20*"*")
    print(20*"*")


@receiver(post_save, sender=OrderItem)
def create_delivery(sender, **kwargs):
    print("create_delivery_group")

    if kwargs.get('created'):
        order_item = kwargs.get('instance')
        delivery_group = order_item.order.delivery_groups.first()
        print("create_delivery_group " + str(delivery_group.pk))
        # import ipdb; ipdb.set_trace()
        delivery = Delivery.objects.create(group=delivery_group, quantity=order_item.quantity, item=order_item)
