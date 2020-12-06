from rest_framework import viewsets
from dm_card.requests.api import serializers
from ..models import Request


class RequestViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.RequestSerializer
    queryset = Request.objects.all()


