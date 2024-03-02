from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from materials.models import Course
from users.models import User, Subscription


class SubscriptionTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email='test@mail.ru')
        self.user.set_password('test')
        self.user.is_superuser = True
        self.user.save()

        self.client.force_authenticate(user=self.user)
        self.course = Course.objects.create(name='Test', description='Test desc', owner=self.user)

    def test_get_subscription_create(self):
        response = self.client.post(
            reverse('users:subscribe'),
            data={"course": self.course.pk}
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )
        self.assertTrue(Subscription.objects.all())

        response = self.client.post(
            reverse('users:subscribe'),
            data={"course": self.course.pk}
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )
        self.assertFalse(Subscription.objects.all())
