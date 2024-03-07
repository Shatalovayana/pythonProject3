from django.shortcuts import get_object_or_404
from django_filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from materials.models import Course
from users.models import User, Subscription, Payments
from users.serializers import UsersSerializer, PaymentsSerializer, SubscriptionSerializer
from users.services import create_stripe_price, create_stripe_product, create_stripe_session


class UsersViewSet(viewsets.ModelViewSet):
    serializer_class = UsersSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]

    def create(self, request):
        serializer = UsersSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        password = serializer.data["password"]
        user = User.objects.get(pk=serializer.data["id"])
        user.set_password(password)
        user.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsAuthenticated]
        return [permission() for permission in self.permission_classes]


class PaymentsCreateAPIView(generics.CreateAPIView):
    serializer_class = PaymentsSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        course = serializer.validated_data["paid_course"]
        stripe_product_id = create_stripe_product(course.name)
        stripe_price_id = create_stripe_price(course.price, stripe_product_id)
        payment_url, payment_id = create_stripe_session(stripe_price_id)
        serializer.save(
            user=self.request.user,
            paid_course=course,
            payment_amount=course.price,
            payment_method='CARD',
            payment_url=payment_url,
            payment_id=payment_id,
            stripe_product_id=stripe_product_id
        )


class PaymentsListAPIView(generics.ListAPIView):
    serializer_class = PaymentsSerializer
    permission_classes = [IsAuthenticated]
    # filter_backends = [DjangoFilterBackend, OrderingFilter]
    # filterset_fields = ('paid_course', 'paid_lesson', 'payment_method')
    # ordering_fields = ('date_of_payment',)
    queryset = Payments.objects.all()
    # def list(self, request, *args, **kwargs):
    #     queryset = super().list(request, args, kwargs)
    #     queryset = queryset.filter(user=self.request.user)
    #     return queryset


class SubscriptionView(APIView):
    serializer_class = SubscriptionSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user

        course_id = request.data.get('course')
        course = get_object_or_404(Course, id=course_id)

        subs_item = Subscription.objects.filter(user=user, course=course)

        if subs_item.exists():
            subs_item.delete()
            message = 'Подписка удалена'

        else:
            Subscription.objects.create(user=user, course=course)
            message = 'Подписка добавлена'

        return Response({"message": message})
