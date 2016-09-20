from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token

from apps.account_balance.api import BalanceViewSet
from apps.address.api import AddressViewSet
from apps.client.api import ClientViewSet
from apps.delivery.api import DeliveryGroupViewSet, DeliveryViewSet, DistributionViewSet

router = DefaultRouter(trailing_slash=False)

router.register(r'account-balances', BalanceViewSet, base_name='account-balances')
router.register(r'addresses', AddressViewSet, base_name='addresses')
router.register(r'clients', ClientViewSet, base_name='clients')
router.register(r'deliveries', DeliveryViewSet, base_name='deliveries')
router.register(r'delivery-groups', DeliveryGroupViewSet, base_name='delivery-groups')
router.register(r'distributions', DistributionViewSet, base_name='distributions')

urlpatterns = [
    url(r'^accounts/', include('rest_auth.urls')),
    url(r'^accounts/registration/', include('rest_auth.registration.urls')),
    url(r'^api-token-auth', obtain_jwt_token),
    # Include router api
    url(r'^', include(router.urls)),
    ]
