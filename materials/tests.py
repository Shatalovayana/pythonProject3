from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from materials.models import Lessons
from users.models import User


class LessonsTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email='test@mail.ru')
        self.user.set_password('test')
        self.user.is_superuser = True
        self.user.save()

        self.client.force_authenticate(user=self.user)
        self.lesson = Lessons.objects.create(name='Test', description='Test', owner=self.user)

    def test_get_lessons_create(self):
        lesson = {
            'name': 'test_lesson',
            'description': 'test_lesson_desc',
        }
        response = self.client.post(
            reverse('materials:lessons-create'),
            lesson
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED,
        )

    def test_get_lessons_list(self):
        response = self.client.get(
            reverse('materials:lessons-list'),
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

    def test_get_lessons_retrieve(self):
        response = self.client.get(
            reverse('materials:lessons-get', kwargs={'pk': self.lesson.pk}),
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

    def test_get_lessons_update(self):
        lesson = {
            'name': 'test_lesson',
            'description': 'test_lesson_desc'
        }
        response = self.client.put(
            reverse('materials:lessons-update', kwargs={'pk': self.lesson.pk}),
            lesson
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

    def test_get_lessons_delete(self):
        lesson = {
            'name': 'test_lesson',
            'description': 'test_lesson_desc'
        }
        response = self.client.delete(
            reverse('materials:lessons-delete', kwargs={'pk': self.lesson.pk}),
            lesson
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT,
        )
