from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from habits.models import Habit
from users.models import User


class HabitTestCase(APITestCase):
    """Тестирование CRUD привычек."""

    def setUp(self):
        self.user = User.objects.create(email='test@mail.ru')
        self.habit = Habit.objects.create(
            user=self.user,
            location='дома',
            time='14:31:00+03:00',
            action='сделать отжимание 50 раз',
            pleasant_habit='False',
            periodicity=1,
            reward='Десерт',
            time_to_complete='00:01:00',
        )
        self.client.force_authenticate(user=self.user)

    def test_habit_list(self):
        url = reverse('habits:habits_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_habit_create(self):
        url = reverse('habits:habits_create')
        data = {
            'user': self.user.pk,
            "location" : "дом",
            "time":"09:00:00+03:00",
            "action":"зарядка утром",
            "pleasant_habit":"False",
            "periodicity":"1",
            "reward":"Игра в PS-5",
            "time_to_complete":"00:01:00"
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habit.objects.all().count(), 2)

    def test_habit_update(self):
        url =  reverse('habits:habits_update', args=(self.habit.pk,))
        data = {
            'user': self.user.pk,
            "location" : "дом",
            "time":"09:00:00+03:00",
            "action":"зарядка утром",
            "pleasant_habit":"False",
            "periodicity":"1",
            "reward":"Прогулка",
            "time_to_complete":"00:01:00"
        }
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get('reward'), 'Прогулка')

    def test_habit_retrieve(self):
        url =  reverse('habits:habits_retrieve', args=(self.habit.pk,))
        response = self.client.get(url)
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("action"), self.habit.action)

    def test_habit_delete(self):
        url = reverse('habits:habits_delete', args=(self.habit.pk,))
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habit.objects.all().count(), 0)

    def test_habit_list_publishing(self):
        url = reverse('habits:publishing_list')
        response = self.client.get(url)
        data = response.json()
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.habit.pk,
                    "location": "дома",
                    "time": "14:31:00",
                    "action": "сделать отжимание 50 раз",
                    "pleasant_habit": False,
                    "periodicity": 1,
                    "reward": "Десерт",
                    "time_to_complete": "00:01:00",
                    "publicity_sign": True,
                    "user": 4,
                    "related_habit": None}
            ]
        }
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)
