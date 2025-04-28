import requests
from config import settings


def send_telegram_message(tg_chat_id, message):
    params = {
        'text': message,
        'chat_id': tg_chat_id,
    }
    requests.get(f'{settings.TELEGRAM_URL} {settings.TELEGRAM_BOT_API}/sendMessage', params=params)