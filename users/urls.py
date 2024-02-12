from django.urls import path
from rest_framework.routers import DefaultRouter

from users.apps import UsersConfig
from users.views import UsersViewSet, PaymentsListAPIView, PaymentsCreateAPIView

app_name = UsersConfig.name

router = DefaultRouter()
router.register(r'users', UsersViewSet, basename='users')

urlpatterns = [
    path('payments/create/', PaymentsCreateAPIView.as_view(), name='payments-create'),
    path('payments/', PaymentsListAPIView.as_view(), name='payments-list'),
] + router.urls
