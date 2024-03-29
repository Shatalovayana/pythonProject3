from django.urls import path
from rest_framework.routers import DefaultRouter

from users.apps import UsersConfig
from users.views import UsersViewSet, PaymentsListAPIView, PaymentsCreateAPIView, SubscriptionView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = UsersConfig.name

router = DefaultRouter()
router.register(r'users', UsersViewSet, basename='users')

urlpatterns = [
    path('payments/create/', PaymentsCreateAPIView.as_view(), name='payments-create'),
    path('payments/', PaymentsListAPIView.as_view(), name='payments-list'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('subscribe/', SubscriptionView.as_view(), name='subscribe'),
    ] + router.urls
