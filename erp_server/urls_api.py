from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token

from apps.account_balance.api import BalanceViewSet

router = DefaultRouter(trailing_slash=False)

router.register(r'sales', BalanceViewSet, base_name='account-balances')

urlpatterns = [
    url(r'^accounts/', include('rest_auth.urls')),
    url(r'^accounts/registration/', include('rest_auth.registration.urls')),
    url(r'^api-token-auth', obtain_jwt_token),
    # Include router api
    url(r'^', include(router.urls)),
    ]
