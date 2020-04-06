from django import forms
from .models import Mercado, Cliente


class mercadoForm(forms.ModelForm):
    class Meta:
        model = Mercado
        fields = ('clientes', 'itens', 'quantidade', 'datacompra', 'endereco')
        field = ('titulo')


class clienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('nome', 'sexo', 'data_nascimento', 'endereco', 'email')