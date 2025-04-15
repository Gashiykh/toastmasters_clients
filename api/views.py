import os
import requests

from rest_framework import views, status
from rest_framework.response import Response

from .serializers import ContactModelSerializer

INSTANCE = os.getenv('GREEN_API_INSTANCE_ID')
TOKEN = os.getenv('GREEN_API_TOKEN')

class ContactAddView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = ContactModelSerializer(data=request.data)
        if serializer.is_valid():
            instance = serializer.save()

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
                print(f"[Green API] Ошибка отправки: {e}")

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
