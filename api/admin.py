import os

import requests
from django.contrib import admin, messages
from .models import Contact

from dotenv import load_dotenv

load_dotenv()

INSTANCE = os.getenv('GREEN_API_INSTANCE_ID')
TOKEN = os.getenv('GREEN_API_TOKEN')

# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    model = Contact
    list_display = ('name', 'phone', 'visit_form', 'club', 'created_at')
    list_filter = ('created_at', 'visit_form',)
    search_fields = ('name', 'phone')


    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)


        if not change:

            url = f"https://api.green-api.com/waInstance{INSTANCE}/sendMessage/{TOKEN}"
            chat_id = f"{obj.phone}@c.us"
            payload = {
                "chatId": chat_id,
                "message": f"Здравствуйте, {obj.name}! Ваши данные успешно сохранены."
            }

            try:
                resp = requests.post(url, json=payload, timeout=10)
                resp.raise_for_status()
            except requests.RequestException as e:
                self.message_user(
                    request,
                    f"Не удалось отправить сообщение через Green API: {e}",
                    level=messages.ERROR,
                )


