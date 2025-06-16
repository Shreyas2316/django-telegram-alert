import requests
import os

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def send_telegram_message(message):
    print("Preparing to send Telegram message...")
    print("TELEGRAM_TOKEN =", TELEGRAM_TOKEN)
    print("TELEGRAM_CHAT_ID =", TELEGRAM_CHAT_ID)
    print("MESSAGE =", message)

    if not TELEGRAM_TOKEN or not TELEGRAM_CHAT_ID:
        raise Exception("Missing TELEGRAM_TOKEN or TELEGRAM_CHAT_ID")

    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message
    }

    response = requests.post(url, data=data)
    print("Telegram API response:", response.status_code, response.text)
    return response.json()
