# app/signals.py
import os
import requests
from dotenv import load_dotenv
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Contact

load_dotenv()

INSTANCE = os.getenv('GREEN_API_INSTANCE_ID')
TOKEN = os.getenv('GREEN_API_TOKEN')


@receiver(post_save, sender=Contact)
def send_whatsapp_message(sender, instance, created, **kwargs):
    if not created:
        return

    phone = instance.phone.replace("+", "").replace(" ", "").strip()
    chat_id = f"{phone}@c.us"
    url = f"https://api.green-api.com/waInstance{INSTANCE}/sendMessage/{TOKEN}"
    payload = {
        "chatId": chat_id,
        "message": f"Здравствуйте, {instance.name}! Ваши данные успешно сохранены."
    }

    try:
        response = requests.post(url, json=payload, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        # Можешь логировать, например:
        print(f"[Green API] Ошибка отправки: {e}")
