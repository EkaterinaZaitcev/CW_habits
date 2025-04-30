import json

from datetime import *
from celery import shared_task

import users
from habits.models import Habit
from habits.services import send_telegram_message

@shared_task
def send_reminder():
    """Напоминание о привычке пользователю в назначенное время"""
    try:
        now = datetime.now()
        time_threshold = now - timedelta(seconds=40)

        habits_to_remind = Habit.objects.filter(
            time__lt=now.time(), time__gt=time_threshold.time()
        )
        for habit in habits_to_remind:
            chat_id = users.tg_chat_id
            if chat_id:
                message = f"Я буду {habit.action} в {habit.time} в {habit.place}"
                send_telegram_message(chat_id, message)
                print("Сообщение отправлено")
    except Habit.DoesNotExist:
        pass