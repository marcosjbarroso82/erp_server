from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token

from apps.account_balance.api import BalanceViewSet
from apps.address.api import AddressViewSet
from apps.client.api import ClientViewSet
from apps.delivery.api import DeliveryGroupViewSet, DeliveryViewSet, DistributionViewSet
from apps.employee.api import EmployeeViewSet
from apps.item_resource.api import ItemResourceViewSet
from apps.order.api import OrderItemViewSet, OrderViewSet
from apps.payment.api import PaymentViewSet
from apps.product.api import ProductViewSet
from apps.provider.api import ProviderViewSet
from apps.stock.api import IOItemResourceStockViewSet, IOProductStockViewSet, ItemResourceStockViewSet, ProductStockViewSet
from apps.cart.api import NewCartViewSet

router = DefaultRouter(trailing_slash=False)

router.register(r'account-balances', BalanceViewSet, base_name='account-balances')
router.register(r'addresses', AddressViewSet, base_name='addresses')
router.register(r'clients', ClientViewSet, base_name='clients')
router.register(r'deliveries', DeliveryViewSet, base_name='deliveries')
router.register(r'delivery-groups', DeliveryGroupViewSet, base_name='delivery-groups')
router.register(r'distributions', DistributionViewSet, base_name='distributions')
router.register(r'employees', EmployeeViewSet, base_name='employees')
router.register(r'item-resource', ItemResourceViewSet, base_name='item-resource')
router.register(r'orders', OrderViewSet, base_name='orders')
router.register(r'order-items', OrderItemViewSet, base_name='order-item')
router.register(r'payments', PaymentViewSet, base_name='payments')
router.register(r'products', ProductViewSet, base_name='products')
router.register(r'providers', ProviderViewSet, base_name='providers')
router.register(r'io-resource-stock', IOItemResourceStockViewSet, base_name='io-resource-stock')
router.register(r'io-product-stock', IOProductStockViewSet, base_name='io-product-stock')
router.register(r'item-resource-stock', ItemResourceStockViewSet, base_name='item-resource-stock')
router.register(r'product-stock', ProductStockViewSet, base_name='product-stock')
router.register(r'new-cart', NewCartViewSet, base_name='new-cart')

urlpatterns = [
    url(r'^accounts/', include('rest_auth.urls')),
    url(r'^accounts/registration/', include('rest_auth.registration.urls')),
    url(r'^api-token-auth', obtain_jwt_token),
    # Include router api
    url(r'^', include(router.urls)),
    ]
