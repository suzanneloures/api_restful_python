from ..models import Request
from rest_framework import serializers


class InputRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = ['name', 'cpf', 'email', 'birth_date','monthly_income']

class OutputRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = ['id', 'name', 'cpf', 'email', 'birth_date', 'created_at', 'monthly_income', 'score', 'is_approved', 'limit_credit']
