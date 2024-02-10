from django_filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics

from users.models import User, Payments
from users.serializers import UsersSerializer, PaymentsSerializer


class UsersViewSet(viewsets.ModelViewSet):
    serializer_class = UsersSerializer
    queryset = User.objects.all()


class PaymentsCreateAPIView(generics.CreateAPIView):
    serializer_class = PaymentsSerializer


class PaymentsListAPIView(generics.ListAPIView):
    serializer_class = PaymentsSerializer
    queryset = Payments.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('paid_course', 'paid_lesson', 'payment_method')
    ordering_fields = ('date_of_payment',)
