from rest_framework import serializers
from cliente.models import Cliente
from cliente.validators import *

class ClienteSerializer(serializers.ModelSerializer):
    """Exibindo todos os clientes"""
    class Meta:
        model = Cliente
        fields = '__all__'
    def validate(self, data):
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({'cpf': "O CPF deve ter 11 dígitos"})
        if not nome_valido(data['nome']):
            raise serializers.ValidationError({'nome': "Não é permitido caracteres numéricos na variável nome!"})
        if not rg_valido(data['rg']):
            raise serializers.ValidationError({'rg': "O RG deve ter 9 dígitos!"})
        return data