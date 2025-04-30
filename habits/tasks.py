from datetime import *
from django.utils import timezone
from celery import shared_task
from habits.models import Habit
from habits.services import send_telegram_message

@shared_task
def send_reminder():
    """Напоминание о привычке пользователю в назначенное время"""

    habits = Habit.objects.all()
    for habit in habits:
        if habit.time <= timezone.now().time():
            tg_chat_id = habit.user.tg_chat_id
            message = f"Пора выполнять: {habit.action}"
            send_telegram_message(tg_chat_id, message)
