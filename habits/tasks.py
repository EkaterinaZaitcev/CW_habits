from datetime import timedelta

from habits.models import Habit
from habits.services import send_telegram_message
from users.models import User


def send_reminder(pk):
    """Напоминание о привычке пользователю в назначенное время"""
    habit = Habit.objects.get(pk=pk)
    text = f'Не забудь {habit.action} в {habit.habit_time + timedelta(hours=1)} {habit.location}'
    send_telegram_message(User.tg_chat_id, text)
