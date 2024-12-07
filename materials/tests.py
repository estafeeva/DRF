from rest_framework import status, serializers
from rest_framework.test import APITestCase

from materials.models import Course, Lesson, Subscription
from users.models import User

from django.urls import reverse


class LessonTestCase(APITestCase):
    # Задаем данные для тестов
    def setUp(self):
        self.user = User.objects.create(email="admin3@example.com")
        self.course = Course.objects.create(
            name="Музыка", description="Курсы по музыке"
        )
        self.lesson = Lesson.objects.create(
            name="Игра на барабанах", course=self.course, owner=self.user
        )
        self.client.force_authenticate(user=self.user)

    def test_lesson_retrieve(self):
        url = reverse("materials:lessons_retrieve", args=(self.lesson.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), self.lesson.name)

    def test_lesson_create(self):
        url = reverse("materials:lessons_create")
        data = {"name": "test", "video_link": "youtube.com"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Lesson.objects.all().count(), 2)

    def test_lesson_update(self):
        url = reverse("materials:lessons_update", args=(self.lesson.pk,))
        data = {"name": "test2", "video_link": "youtube.com"}
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), "test2")

    def test_lesson_delete(self):
        url = reverse("materials:lessons_delete", args=(self.lesson.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Lesson.objects.all().count(), 0)

    def test_lesson_list(self):
        url = reverse("materials:lessons_list")
        response = self.client.get(url)
        data = response.json()
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.lesson.pk,
                    "video_link": None,
                    "name": self.lesson.name,
                    "description": None,
                    "preview": None,
                    "course": self.course.pk,
                    "owner": self.user.pk,
                }
            ],
        }
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)


class SubscriptionTestCase(APITestCase):
    def setUp(self):
        # Задаем данные для тестов
        self.user = User.objects.create(
            email="admin3@example.com", is_staff=False, is_superuser=False
        )
        self.course = Course.objects.create(
            name="Музыка", description="Курсы по музыке", owner=self.user
        )
        self.lesson = Lesson.objects.create(
            name="Игра на барабанах", course=self.course, owner=self.user
        )
        self.client.force_authenticate(user=self.user)
        self.subscription = Subscription.objects.create(
            course=self.course, user=self.user
        )

    def test_subscription(self):
        url = reverse("materials:subscription")
        data = {"course": self.course.pk}
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get("message"), "Подписка отключена")

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get("message"), "Подписка включена")
