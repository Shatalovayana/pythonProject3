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

    def test_get_lessons_create(self):
        lesson = Lessons.objects.create(
            name='test_lesson',
            description='test_lesson_desc',
            link='https://www.youtube.com/'
        )
        response = self.client.post(
            reverse('materials:lessons-create'),
            lesson
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED,
        )

    def test_get_lessons_list(self):
        lesson = Lessons.objects.create(
            name='test_lesson',
            description='test_lesson_desc',
            link='https://www.youtube.com/'
        )
        response = self.client.get(
            reverse('materials:lessons-list'),
            lesson
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

    def test_get_lessons_retrieve(self):
        lesson = Lessons.objects.create(
            name='test_lesson',
            description='test_lesson_desc',
            link='https://www.youtube.com/'
        )
        response = self.client.get(f'/lesson/{lesson.pk}/')
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

    def test_get_lessons_update(self):
        lesson = Lessons.objects.create(
            name='test_lesson',
            description='test_lesson_desc',
            link='https://www.youtube.com/'
        )
        updated_lesson = {
            'name': 'updated name',
            'description': 'updated description',
            'link': 'https://www.youtube.com/'
        }
        response = self.client.put(
            f'/lesson/update/{lesson.pk}/',
            data=updated_lesson,
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_get_lessons_destroy(self):
        lesson = Lessons.objects.create(
            name='test_lesson_for_delete',
            description='test_lesson_desc_for_delete',
            link='https://www.youtube.com/'
        )
        response = self.client.delete(
            f'/lesson/delete/{lesson.pk}/',
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
