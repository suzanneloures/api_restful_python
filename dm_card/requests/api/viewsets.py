from rest_framework import viewsets
from .serializers import InputRequestSerializer, OutputRequestSerializer
from ..models import Request
from rest_framework.response import Response
from rest_framework import status
import random
from decimal import Decimal



class RequestViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Request.objects.all()
        serializer = InputRequestSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = InputRequestSerializer(data=request.data)
        if serializer.is_valid():
            score = self.verify_score()
            is_approved = self.is_approved(score)
            if is_approved == 1:
                monthly_income = serializer.validated_data['monthly_income']
                limit_credit = self.calculate_limit_credit(score,monthly_income)
                serializer.save(score=score,is_approved=is_approved, limit_credit=limit_credit)
                return Response({"msg": "Sua solicitação foi: Aprovada"},status=status.HTTP_200_OK)
            elif is_approved == 0:
                serializer.save(score=score,is_approved=is_approved)
                return Response({"msg": "Sua solicitação foi: Reprovada"},status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        

    def destroy(self, request, pk=None):
        pass

    def verify_score(self):
        score = random.randint(1, 999)
        return score
    
    def is_approved(self, score):
        if score <= 299:
            is_approved = 0
        elif score >= 300:
            is_approved = 1
        return is_approved
   
    def calculate_limit_credit(self, score, monthly_income):
        monthly_income = self.convert_string_to_decimal(monthly_income)
        if score >= 300 and score <= 599:
            limit_credit = 1000
        elif score >= 600 and score <= 799:
            limit_credit = int(monthly_income)/2
            if limit_credit > 1000:
                limit_credit = 1000
        elif score >= 800 and score <= 950 :
            limit_credit = int(monthly_income) * 2
        elif score >= 951:
            limit_credit = 1000000
        return limit_credit

    def convert_string_to_decimal(self, string):
        string_in_decimal = Decimal(string)
        return string_in_decimal



