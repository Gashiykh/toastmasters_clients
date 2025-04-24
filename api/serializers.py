from rest_framework import serializers

from .models import Contact

class ContactModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = [
            'id',
            'name',
            'phone',
            'visit_form',
            'is_toastmasters',
            'club',
            'created_at'
        ]

    def validate(self, data):
        is_toastmasters = data.get('is_toastmasters')
        club = data.get('club')

        if is_toastmasters and not club:
            raise serializers.ValidationError({
                'club': "Please provide your Toastmasters club name."
            })
        return data


class BroadcastSerializer(serializers.Serializer):
    message = serializers.CharField(max_length=2000, required=False)

    def validate(self, data):
        if not data.get('message'):
            data['message'] = DEFAULT_TEMPLATE
        return data

DEFAULT_TEMPLATE = """Dear {name},
Only 2 days to go until *Nomads of the Digital Era: Speak, Lead, Innovate* —
the very first international Toastmasters conference in Kazakhstan! 🇰🇿✨

📌 *Event Details*
• Date: April 26, 2025
• Format: In-person Conference
• Location: KIMEP University, Almaty

We can’t wait to welcome you to a day full of powerful speeches, leadership insights, and meaningful connections. 💬🤝

✨ Tomorrow we’ll share the full agenda and practical info.
🔗 The conference link will be sent on the event day.

Get ready to be inspired!
"""