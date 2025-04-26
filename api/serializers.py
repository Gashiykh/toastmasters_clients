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
🎉 Today’s the day! 🎉
Welcome to Nomads of the Digital Era: Speak, Lead, Innovate — the first-ever international Toastmasters conference in Kazakhstan!

📍 Location: KIMEP University, Almaty
📅 Date: April 26, 2025
⏰ 9:00
Whether you're here to learn, to lead, or to be inspired — this is your moment.

Here is Today's Agenda:
https://shorturl.at/lbP28

🔗 Here’s the conference link: 
https://shorturl.at/cxPVA

Let’s make history together! 🚀🎙
"""
