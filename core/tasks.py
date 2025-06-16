from celery import shared_task
from .telegram_utils import send_telegram_message
from .models import TelegramLog 

@shared_task
def print_message():
    print("This is a Celery background task running!")
    return "Task completed"

@shared_task
def send_alert(message):
    print("Sending to Telegram:", message)
    send_telegram_message(message)
    TelegramLog.objects.create(message=message) 
    return "Telegram alert sent and logged."
