from rest_framework import viewsets
from .serializers import InputRequestSerializer, OutputRequestSerializer
from ..models import Request
from rest_framework.response import Response
from rest_framework import status
import random
from ..services import SolicitationService




class RequestViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Request.objects.all()
        serializer = OutputRequestSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = InputRequestSerializer(data=request.data)
        if serializer.is_valid():
            score = self.verify_score()
            is_approved = self.is_approved(score)
            if is_approved == 1:
                monthly_income = serializer.validated_data['monthly_income']
                limit_credit = SolicitationService.calculate_limit_credit(score,monthly_income)
                serializer.save(score=score,is_approved=is_approved, limit_credit=limit_credit)
                return Response({"msg": "Sua solicitação foi Aprovada"},status=status.HTTP_200_OK)
            elif is_approved == 0:
                serializer.save(score=score,is_approved=is_approved)
                return Response({"msg": "Sua solicitação foi Reprovada"},status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        

    def destroy(self, request, pk=None):
        queryset = Request.objects.get(pk=pk)
        queryset.delete()
        return Response({"msg": "Solicitação excluida com sucesso"},status=status.HTTP_200_OK)
        
    def verify_score(self):
        score = random.randint(1, 999)
        return score
    
    def is_approved(self, score):
        if score <= 299:
            is_approved = 0
        elif score >= 300:
            is_approved = 1
        return is_approved




