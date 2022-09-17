from django.db import models

class categoria(models.Model):

    nome= models.CharField(max_length=100)
    dt_criacao = models.DateTimeField(auto_now_add=True)

class transacao(models.Model):
    
    data = models.DateTimeField(auto_now_add=True)
    descricao= models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    


    


