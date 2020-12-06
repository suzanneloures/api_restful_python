from django.db import models

class Request(models.Model):
    name = models.CharField(max_length=200)
    cpf = models.CharField(max_length=11)
    email = models.EmailField(max_length=254)
    birth_date = models.DateField(auto_now=False)
    created_at = models.DateTimeField(auto_now_add=True)