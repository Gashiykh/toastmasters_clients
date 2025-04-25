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

DEFAULT_TEMPLATE = """Dear [Name],
The countdown is almost over — just 1 day left until Nomads of the Digital Era: Speak, Lead, Innovate! 🎉
We’re thrilled to invite you to the first international Toastmasters conference ever held in Kazakhstan — a celebration of voice, vision, and transformation.
📌 When & Where:
• Date: April 26, 2025
• Location: KIMEP University, Almaty
🎤 Today, you’ll receive the full schedule and speaker lineup.
📬 And tomorrow morning, we’ll send you the final access link.
Get ready to connect, grow, and be part of something unforgettable! 💡🌍
"""