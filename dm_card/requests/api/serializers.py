from ..models import Request
from rest_framework import serializers


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = ['name', 'cpf', 'email', 'birth_date', 'created_at']

