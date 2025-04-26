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
Links for joining online livestreams of next speaker sessions:

Hall #1:
Panel Discussion: "ИИ заменит нас: правда или ложь" (Russian)
1) Zhuldyz Saulebekova (Almaty Air Initiative)
2) Arman Shokparov (People Consulting Ltd.)
3) Mark Inger (Pleep)
4) Nik McFly (Hybrain.ai (https://hybrain.ai/) n Ailand)
5) Daniyar Abenov (Postureletics)
Link: https://shorturl.at/cxPVA

Hall #2
Nuraly Begaliev (Teknolab), "Бірінші кадамнын куші" (Kazakh)
Eskendir Bestai (Ustart.kz (https://ustart.kz/)) "МарапаПЕН жазалау" (Kazakh)
Link: https://meet.google.com/ovk-zofq-pcx

Hall #4
Regina Andreyeva (Pincode), "Выбирай себя: карьерный мастер класс" (Russian)
Link: https://meet.google.com/fyd-uwbq-qcs
"""
