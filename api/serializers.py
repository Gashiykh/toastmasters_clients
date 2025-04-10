from rest_framework import serializers

from .models import Contact

class ContactModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'name', 'phone', 'created_at']

