from rest_framework import serializers
from .models import Cliente, Veiculos, Entrada, ENTRADA_CHOICES, PATIO_CHOICES, STATUS_CHOICES, VEICULO_CHOICES


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'


class VeiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Veiculos
        fields = '__all__'


class EntradaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entrada
        fields = '__all__'