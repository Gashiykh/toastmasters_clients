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

DEFAULT_TEMPLATE = """
Here are the links to online livestream of our speakers:

🎤 Speaker: Sabina Lonjon (Mars Wrigley)
📝 Topic: "The truth behind FMCG marketing: lessons I've learned along the way" (Session in English)
🔗 Link: https://meet.google.com/ovk-zofq-pcx


🎤 Speaker: Indira Kyilybaeva (Glovo, Finmentor)
📝 Topic: "From Speaking to Doing" (English)
🔗 Link: https://shorturl.at/cxPVA
"""
