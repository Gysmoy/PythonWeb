from rest_framework import serializers

class setCycles(serializers.Serializer):
    tipo = serializers.CharField(max_length = 15)
    ciclo = serializers.CharField(max_length = 10)

class updateCycle(serializers.Serializer):
    id = serializers.CharField(max_length = 10)
    tipo = serializers.CharField(max_length = 50)
    ciclo = serializers.CharField(max_length = 10)

class idCycle(serializers.Serializer):
    id = serializers.CharField(max_length = 20)

