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
        print(f"{response.status_code}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_habit_create(self):
        url = reverse('habits:habits_create')
        data = {
            'user': self.user.pk,
            'location': 'дома',
            'time': '14:32:00+03:00',
            'action': 'выпить чашечку кофе',
            'sign_of_habit': 'True',
            'periodicity': 1,
            'time_to_complete': '00:02:00',
        }
        response = self.client.post(url, data)
        print(f'{response}')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habit.objects.all().count(), 1)
