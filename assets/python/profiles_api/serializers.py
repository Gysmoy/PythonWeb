from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    '''Serializar una campo para probar nuestro APIView'''
    name = serializers.CharField(max_length=100)