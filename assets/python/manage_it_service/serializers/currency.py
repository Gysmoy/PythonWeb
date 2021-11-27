from rest_framework import serializers

class setCurrencySerializer(serializers.Serializer):
    moneda = serializers.CharField(max_length = 12)
    estado = serializers.ChoiceField(choices = (('1', 'ACTIVO'), ('0', 'INACTIVO')))

class updateCurrencySerializer(serializers.Serializer):
    id = serializers.CharField(max_length = 8)
    moneda = serializers.CharField(max_length = 12)

class idCurrency(serializers.Serializer):
    id = serializers.CharField(max_length = 8)
