import os
import requests

from rest_framework import views, status
from rest_framework.response import Response

from .models import Contact
from .serializers import ContactModelSerializer, BroadcastSerializer
from .utils import normalize_phone, send_whatsapp

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

April 26th 2025, 9:00
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


class BroadcastView(views.APIView):

    def post(self, request, *args, **kwargs):
        serializer = BroadcastSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        template = serializer.validated_data["message"]

        contacts = Contact.objects.all().iterator()
        sent, failed = 0, 0

        for contact in contacts:
            msg = template.format(name=contact.name)
            chat_id = normalize_phone(contact.phone)

            try:
                send_whatsapp(chat_id, msg)
                sent += 1
            except Exception as exc:
                failed += 1

                print(f"Error sending message to {contact.name} (ID: {contact.id}) with phone {contact.phone}: {exc}")

        return Response(
            {"sent": sent, "failed": failed},
            status=status.HTTP_200_OK,
        )
