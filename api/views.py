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
            print(1111)
            phone = instance.phone.replace("+", "").replace(" ", "").strip()
            chat_id = f"{phone}@c.us"
            url = f"https://api.green-api.com/waInstance{INSTANCE}/sendMessage/{TOKEN}"
            payload = {
                "chatId": chat_id,
                "message": f"""Welcome to "Nomads of the Digital Era"! 🌍🚀

Dear {instance.name},

Thank you for registering for the "Nomads of the Digital Era" conference! We're excited to have you join us for inspiring talks, engaging workshops, and valuable networking with global digital pioneers. Stay tuned for more details as we approach the event date. 

We can't wait to see you there!

April 26th 2025,
KIMEP Univesity, New building, Abay st. 2 
Almaty, Kazakhstan

Best regards,
The Nomads of the Digital Era Team
                    """
            }
            print(222)

            try:
                response = requests.post(url, json=payload, timeout=10)
                print(response)
                print(response.text)
                response.raise_for_status()
            except requests.RequestException as e:
                print(f"[Green API] Ошибка отправки: {e}")

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
