from decimal import Decimal

class SolicitationService:

    @staticmethod
    def calculate_limit_credit(score, monthly_income):
        monthly_income = Decimal(monthly_income)
        if score >= 300 and score <= 599:
            limit_credit = 1000
        elif score >= 600 and score <= 799:
            limit_credit = int(monthly_income)/2
            if limit_credit < 1000:
                limit_credit = 1000
        elif score >= 800 and score <= 950 :
            limit_credit = int(monthly_income) * 2
        elif score >= 951:
            limit_credit = 1000000
        return limit_credit




