from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    '''Serializar una campo para probar nuestro APIView'''
    name = serializers.CharField(max_length=100)
    apellido = serializers.CharField(max_length=100)
    telefono = serializers.CharField(max_length=100)
    gmail = serializers.CharField(max_length=100)
    edad = serializers.CharField(max_length=100)

class UserSerializer(serializers.Serializer):
    '''SERIALIZA UN CAMPO'''
    id = serializers.CharField(max_length = 8)
    search = serializers.CharField(max_length = 50)
    username = serializers.CharField(max_length = 320)
    password = serializers.CharField(max_length = 64)

class LoginSerializer(serializers.Serializer):
    '''Datos que vienen del login'''
    username = serializers.CharField(max_length = 320)
    password = serializers.CharField(max_length = 64)