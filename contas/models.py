from django.db import models

class Cliente(models.Model):
    SEXO_CHOICES = (
        ("F", "Feminino"),
        ("M", "Masculino"),
        ("N", "Nenhuma das opções")
    )
    nome = models.CharField(max_length=100)
    sexo = models.CharField(max_length=20, choices=SEXO_CHOICES, default='M', blank=True)
    data_nascimento = models.DateField(null=True, blank=True)
    email = models.EmailField(max_length=255, validators=() ,null=True, blank=True)
    data = models.DateTimeField(auto_now=True)
    endereco = models.CharField(max_length=100, null=True)


    def __str__(self):
        return self.nome


class Mercado(models.Model):
    clientes = models.ForeignKey('Cliente', on_delete=models.SET_NULL, null=True)
    endereco = models.CharField(max_length=100, null=True)
    ITENS_CHOICES = (
        ("F", "Frango"),
        ("M", "Maionese"),
        ("C", "Carne"),
        ("T", "Tomate"),
        ("A", "Arroz"),
        ("FE", "Feijão"),
        ("FR", "Frios"),
        ("B", "Bebidas"),
        ("N", "Nenhuma das opções")
    )
    itens = models.CharField(max_length=255, choices=ITENS_CHOICES, default='N', blank=True)
    quantidade = models.IntegerField(null=True)
    datacompra = models.DateField(auto_now_add=False)
    data = models.DateTimeField(auto_now=True)
    
    
   
    def __str__(self):
        return self.pk


